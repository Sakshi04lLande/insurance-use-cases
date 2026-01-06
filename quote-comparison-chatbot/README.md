# GenAI Insurance Quote Comparison Assistant

## Project Overview

GenAI Insurance Quote Comparison Assistant is a GenAI-based system that helps users compare
insurance quotes **before purchasing a policy**.

Insurance quotes often contain complex coverage details, limits, co-payments, and conditions
that are difficult for customers to understand. This project reads insurance quote PDFs and
explains differences between plans in **clear and simple language**.

The system focuses on **future risk coverage**, helping users understand which policy offers
better protection based on the available document information, without making assumptions.

---

## Input

- Insurance quote document in **PDF format**
- The document may contain:
  - Multiple insurance plans
  - Coverage details
  - Co-payments / deductibles
  - Limits and conditions
  - Waiting periods

Supported examples:
- Health insurance quote PDFs  
- Multi-plan comparison documents  
- Hospitalisation and treatment coverage quotes  

---

## Output

The system generates a **short and decision-focused response** containing:

- **Coverage Comparison** – key differences between plans  
- **Cost Insight** – co-payments / deductibles and limits  
- **Recommendation** – most suitable plan based on document facts  
- **Important Notes** – waiting periods or limitations if mentioned  

All outputs are strictly grounded in the document and kept concise.

---

## Technology Used

- Python  
- Azure OpenAI (Large Language Model)  
- LangChain (Retrieval-Augmented Generation)  
- ChromaDB (Vector Database)  
- HuggingFace Embeddings  
- pdfplumber  
- dotenv  

---

## How It Works

- User uploads an insurance quote PDF  
- The document is split into chunks and embedded  
- Relevant sections are retrieved using similarity search  
- AI compares plans using only retrieved content  
- No assumptions or external knowledge is used  
- Final recommendation is returned in clear, short text  

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
python app.py
