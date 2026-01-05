#  Policy Summary Assistant (GenAI)

##  Project Overview
Policy Summary Assistant is a GenAI-based tool that reads long insurance policy PDFs and generates a **clear, plain-language summary**.  
It helps users quickly understand **coverage, exclusions, limits, and conditions** without reading the full policy document.

The system is designed to be **neutral, safe, and factual**, using a two-step AI process to avoid assumptions or misleading summaries.

---

##  Input
- Insurance policy document in **PDF format**
- Supported examples:
  - Health Insurance Policies  
  - Group Insurance Policies  
  - Contractors All Risks Policies  

---

##  Output
A structured policy summary containing:
- **Scope** – what type of document it is  
- **Coverage** – high-level benefits (plain language)  
- **Exclusions** – major non-covered areas  
- **Limits & Conditions** – important claim-related rules  
- **Missing Information** – details not available in the document  

---
## Technology Used
-Python
-Streamlit (UI)
-Azure OpenAI (LLM)
-LangChain (prompt control & chunking)
-pdfplumber (PDF text extraction)
-dotenv (environment configuration)

##  How It Works
1. Extracts text from the uploaded PDF  
2. Splits content into safe-sized chunks  
3. **Stage 1:** Extracts factual notes (no interpretation)  
4. **Stage 2:** Generates a controlled, plain-language summary  
5. Displays the final summary in a clean UI  

---

## How to Run
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add Azure OpenAI credentials in .env file

# Run the app
streamlit run app.py
