import os
import pdfplumber
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI

# =====================================================
# LOAD ENV VARIABLES
# =====================================================
load_dotenv()

# =====================================================
# PROMPT TEMPLATE
# =====================================================
CLAIM_PROMPT = PromptTemplate(
    input_variables=["claim_text", "decision"],
    template="""
You are an insurance claim explanation assistant.

Your task is to explain the claim settlement outcome
to a customer in very simple and polite language.

Rules:
- Use easy English
- Do NOT use legal or insurance terms
- Never blame the customer
- Clearly explain why the claim was {decision}
- Keep the explanation short (under 120 words)
- Maintain a calm and respectful tone

Claim Report:
{claim_text}

Customer-Friendly Explanation:
"""
)

# =====================================================
# READ PDF
# =====================================================
def extract_text_from_pdf(pdf_path: str) -> str:
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

# =====================================================
# LLM SETUP
# =====================================================
def get_llm():
    return AzureChatOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        api_version=os.getenv("AZURE_OPENAI_VERSION"),
        temperature=0.4
    )

# =====================================================
# MAIN FUNCTION
# =====================================================
def explain_claim(pdf_path: str, decision: str) -> str:
    claim_text = extract_text_from_pdf(pdf_path)
    llm = get_llm()

    chain = CLAIM_PROMPT | llm

    response = chain.invoke({
        "claim_text": claim_text,
        "decision": decision
    })

    return response.content
