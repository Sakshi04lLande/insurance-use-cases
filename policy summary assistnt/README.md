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
