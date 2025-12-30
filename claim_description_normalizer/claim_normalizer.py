import os
from typing import List
from dotenv import load_dotenv
from pydantic import BaseModel

from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate

# ======================================================
# LOAD ENV VARIABLES
# ======================================================
load_dotenv()

# ======================================================
# AZURE OPENAI LLM (CORRECT CONFIG)
# ======================================================
llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_VERSION"),
    temperature=0.0
)

# ======================================================
# OUTPUT SCHEMA (STRICT)
# ======================================================
class ClaimOutput(BaseModel):
    loss_type: str | None
    severity: str | None
    affected_assets: List[str]
    incident_summary: str | None

# ======================================================
# PROMPT TEMPLATE (NO JSON INSTRUCTIONS NEEDED)
# ======================================================
PROMPT = PromptTemplate(
    input_variables=["claim_text"],
    template="""
You are an insurance claims AI system.

Extract structured claim information ONLY from the text.

Rules:
- Do NOT assume facts
- Do NOT infer missing data
- If information is missing, return null

Claim Text:
\"\"\"{claim_text}\"\"\"
"""
)

# ======================================================
# MAIN FUNCTION (✔ GUARANTEED VALID JSON)
# ======================================================
def normalize_claim_description(claim_text: str) -> dict:
    structured_llm = llm.with_structured_output(ClaimOutput)

    chain = PROMPT | structured_llm

    result: ClaimOutput = chain.invoke({"claim_text": claim_text})

    return result.model_dump()
