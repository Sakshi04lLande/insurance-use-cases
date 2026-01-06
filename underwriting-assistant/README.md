# GenAI Underwriting Assistant

## Project Overview

 Underwriting Assistant is a GenAI-based system that helps insurance underwriters
assess applicant risk **before approving or pricing a policy**.

Traditional underwriting systems rely on fixed, hardcoded rules.
This project uses a **document-driven approach**, where underwriting guidelines are read
from documents and interpreted using a Large Language Model (LLM).

The system analyzes applicant data, claims history, and external risk indicators to
generate a **clear, explainable underwriting decision** without making assumptions.

---

## Input

- Applicant details:
  - Age
  - Occupation
  - Annual income
  - Credit score
  - Location risk zone
- Claims history (if any)
- External risk indicators:
  - Fraud flag
  - Medical risk level
- Underwriting guidelines document (text-based)

Supported scenarios:
- Health insurance underwriting  
- Life insurance risk assessment  
- General insurance applicant screening  

---

## Output

The system generates a **clear and structured underwriting decision** containing:

- **Risk Score** – numeric score between 0 and 100  
- **Risk Category** – Low / Medium / High  
- **Underwriting Recommendation** – approve, review, or reject  
- **Justification** – simple explanation based on retrieved guidelines  

All outputs are strictly grounded in the underwriting document and applicant data.

---

## Technology Used

- Python  
- Azure OpenAI (Large Language Model)  
- LangChain (Retrieval-Augmented Generation)  
- ChromaDB (Vector Database)  
- HuggingFace Embeddings  
- Streamlit  
- dotenv  

---

## How It Works

- Underwriting guidelines are stored in an external document  
- The document is converted into embeddings and stored in ChromaDB  
- Applicant details are used to retrieve relevant guideline sections  
- Azure OpenAI analyzes:
  - Applicant profile
  - Claims history
  - External risk indicators
  - Retrieved underwriting guidelines  
- The system generates a structured, explainable underwriting decision  
- No hardcoded rules or external assumptions are used  

---

## How to Run the Project

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add Azure OpenAI credentials in .env file

# Run the application
streamlit run app.py
