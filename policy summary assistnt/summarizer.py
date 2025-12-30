
# Policy Summary Assistant 
# =========================================================
import os
import pdfplumber
from dotenv import load_dotenv
from typing import List

from langchain_openai import AzureChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================
load_dotenv()

llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    openai_api_version=os.getenv("AZURE_OPENAI_VERSION"),
    temperature=0.1
)

# =========================================================
# STAGE 1 — FACT EXTRACTION PROMPT 
# =========================================================
FACT_EXTRACTION_PROMPT = PromptTemplate(
    input_variables=["text"],
    template="""
You are a document analysis assistant performing neutral information extraction.

Disclaimer: This is not legal, medical, or financial advice. You are extracting facts only, not interpreting content.

Task:
Extract only factual statements explicitly stated in the document.

Rules:
- Extract facts exactly as written
- Do not summarize, infer, or rephrase
- Do not add explanations
- Mark unclear/absent information as "Not Mentioned"

Return bullet points under these headings (only if present):

- Document Role
- Policy Category  
- Coverage Mentions
- Exclusion Mentions
- Limits / Conditions Mentions
- Missing / Not Mentioned Items

Text to analyze:
{text}
"""
)

# =========================================================
# STAGE 2 — FINAL SUMMARY PROMPT 
# =========================================================
FINAL_SUMMARY_PROMPT = PromptTemplate(
    input_variables=["notes"],
    template="""
You are an insurance policy analyst.

Your task is to write a clear, neutral, plain-language summary of the policy
based ONLY on the extracted notes provided.

IMPORTANT:
- This summary is for understanding the document only.
- It does NOT confirm, promise, or guarantee coverage.

WRITING STYLE (MANDATORY):
- Write like a professional insurance analyst, not a chatbot.
- Be concise, factual, and structured.
- Avoid long lists, medical jargon, and excessive examples.
- Group similar items instead of enumerating them.
- Use cautious language: "generally", "may", "subject to", "as per policy terms".
- Do NOT assume standard insurance benefits.
- If something is unclear or missing, say so explicitly.

LENGTH CONTROL (STRICT):
- Total length: 150-200 words.
- Coverage: maximum 3-4 bullets.
- Exclusions: maximum 2-3 bullets.
- Limits & Conditions: maximum 3 bullets.
- Missing Information: maximum 2 bullets.
- Each bullet must be ONE sentence only.

OUTPUT FORMAT (MANDATORY):

Scope:
Briefly state what this document is (policy / endorsement / annexure),
the insurance category, and that the summary is based only on the provided text.

Coverage:
- Summarize the main types of coverage at a high level.
- Do NOT list diseases or procedures unless unavoidable.

Exclusions:
- Summarize major exclusion categories only.

Limits & Conditions:
- Highlight only conditions that materially affect claims or coverage.

Missing Information:
- Clearly state important details that are not available in this document
  (e.g., sums insured, schedules, employer selections).

Closing Note:
This summary is for informational purposes only and does not guarantee coverage.
Actual benefits, limits, and conditions are governed by the complete policy documentation.

EXTRACTED NOTES:
{notes}
"""
)

# =========================================================
# PDF TEXT EXTRACTION
# =========================================================
def extract_text_from_pdf(pdf_path: str) -> str:
    full_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"

    return full_text


# =========================================================
# SPLIT DOCUMENT INTO SAFE CHUNKS 
# =========================================================
def split_into_chunks(text: str) -> List[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,      
        chunk_overlap=100
    )
    return splitter.split_text(text)


# =========================================================
# STAGE 1 — FACT EXTRACTION WITH ERROR HANDLING
# =========================================================
def extract_facts_from_chunks(chunks: List[str]) -> str:
    extracted_notes = []

    for idx, chunk in enumerate(chunks):
        try:
            response = llm.invoke(
                FACT_EXTRACTION_PROMPT.format(text=chunk)
            )
            extracted_notes.append(response.content)

        except ValueError:
            # Azure content filter triggered
            extracted_notes.append(
                f"- [Chunk {idx + 1} skipped due to Azure content moderation]"
            )

        except Exception as e:
            # Any unexpected error
            extracted_notes.append(
                f"- [Chunk {idx + 1} failed due to unexpected error]"
            )

    return "\n".join(extracted_notes)


# =========================================================
# STAGE 2 — FINAL SUMMARY GENERATION
# =========================================================
def generate_policy_summary(pdf_path: str) -> str:
    # Step 1: Extract raw text
    raw_text = extract_text_from_pdf(pdf_path)

    if not raw_text.strip():
        return "No readable text found in the document."

    # Step 2: Split into chunks
    chunks = split_into_chunks(raw_text)

    # Step 3: Extract factual notes
    merged_notes = extract_facts_from_chunks(chunks)

    # Step 4: Generate final summary
    try:
        final_response = llm.invoke(
            FINAL_SUMMARY_PROMPT.format(notes=merged_notes)
        )
        return final_response.content

    except ValueError:
        return "Summary could not be generated due to Azure content moderation."

    except Exception:
        return "An unexpected error occurred while generating the summary."
