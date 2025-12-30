import os
import pdfplumber
from dotenv import load_dotenv

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import AzureChatOpenAI
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter


# --------------------------------------------------
# Load environment variables
# --------------------------------------------------
load_dotenv()

# --------------------------------------------------
# Load insurance quotes from PDF
# --------------------------------------------------
def load_quotes_from_pdf(pdf_path: str) -> str:
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

# --------------------------------------------------
# Dynamic Prompt
# --------------------------------------------------
INSURANCE_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an insurance recommendation assistant.

STRICT RULES (must follow):
- Use ONLY the provided document context.
- Do NOT assume or invent information.
- Keep the TOTAL response within 2–4 short lines.
- Each section must be ONE concise sentence only.
- If information is unclear, say so briefly in Limitations.
- Recommend ONLY ONE plan.

Output format (STRICT — no extra text):

Summary: <1 short factual line from the document>
Comparison: <1 short line explaining key difference>
Recommendation: <Plan name> — <reason in 1 line>
Limitations: <1 short limitation from document>

Document Context:
{context}

User Question:
{question}

Answer:

"""
)

# --------------------------------------------------
# Create RAG pipeline
# --------------------------------------------------
def create_rag_pipeline(pdf_path: str):

    raw_text = load_quotes_from_pdf(pdf_path)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=150
    )
    documents = splitter.create_documents([raw_text])

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory="./chroma_db",
    collection_name="insurance_quotes_v1"
)


    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    llm = AzureChatOpenAI(
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
        openai_api_version=os.environ["AZURE_OPENAI_VERSION"],
        temperature=0.2
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type_kwargs={"prompt": INSURANCE_PROMPT}
    )

    return qa_chain
