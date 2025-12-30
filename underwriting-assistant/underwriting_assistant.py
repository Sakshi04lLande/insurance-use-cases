# =========================================================
# GENAI UNDERWRITING ASSISTANT 
# =========================================================

import os
import json
from dotenv import load_dotenv
from pydantic import BaseModel, Field

from langchain_openai import AzureChatOpenAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

# =========================================================
# LOAD ENV
# =========================================================
load_dotenv()

# =========================================================
# LLM CONFIG
# =========================================================
llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    openai_api_version=os.getenv("AZURE_OPENAI_VERSION"),
    temperature=0
)

# =========================================================
# LOAD UNDERWRITING DOCUMENTS 
# =========================================================
def load_guidelines(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

guidelines_text = load_guidelines("underwriting_guidelines.txt")

# =========================================================
# VECTOR STORE (RAG)
# =========================================================
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    collection_name="underwriting_guidelines",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)

vectorstore.add_texts([guidelines_text])
vectorstore.persist()

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# =========================================================
# OUTPUT SCHEMAS
# =========================================================
class UnderwritingDecision(BaseModel):
    risk_score: int = Field(ge=0, le=100)
    risk_category: str
    underwriting_recommendation: str
    justification: str

decision_parser = PydanticOutputParser(pydantic_object=UnderwritingDecision)

# =========================================================
# FINAL PROMPT 
# =========================================================
decision_prompt = PromptTemplate(
    template="""
You are a senior insurance underwriter.

Use the underwriting guidelines provided to assess the applicant.
Do NOT invent rules.
Base your reasoning strictly on the retrieved guidelines and applicant data.

Underwriting Guidelines:
{guidelines}

{format}

Applicant Profile:
{applicant}

Claims History:
{claims}

External Risk Indicators:
{external}
""",
    input_variables=["applicant", "claims", "external", "guidelines"],
    partial_variables={"format": decision_parser.get_format_instructions()}
)

final_chain = decision_prompt | llm | decision_parser

# =========================================================
# MAIN FUNCTION
# =========================================================
def underwriting_assistant(input_data: dict) -> UnderwritingDecision:

    # 🔍 Context-aware retrieval query
    query = f"""
    Credit score: {input_data['applicant']['credit_score']}
    Occupation: {input_data['applicant']['occupation']}
    Claims count: {len(input_data['claims_history'])}
    Medical risk: {input_data['external_reports']['medical_risk']}
    Fraud flag: {input_data['external_reports']['fraud_flag']}
    """

    docs = retriever.invoke(query)
    guidelines_context = "\n".join(doc.page_content for doc in docs)

    decision = final_chain.invoke({
        "applicant": json.dumps(input_data["applicant"], indent=2),
        "claims": json.dumps(input_data["claims_history"], indent=2),
        "external": json.dumps(input_data["external_reports"], indent=2),
        "guidelines": guidelines_context
    })

    return decision
