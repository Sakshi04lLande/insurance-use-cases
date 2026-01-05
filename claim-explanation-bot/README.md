#  GenAI Claim Explanation Bot

## Project Overview

GenAI Claim Explanation Bot is a GenAI-based tool that explains **insurance claim settlement outcomes** to customers in clear, simple, and customer-friendly language.

It helps users understand **why their claim was approved, reduced, or denied** without reading complex claim reports or policy terms.

The system is designed to be **neutral, polite, and factual**, focusing on tone adaptation and summarization so that explanations are easy to understand and trustworthy.

---

##  Input

- Insurance claim report in **PDF format**
- Claim decision selected by the user:
  - Approved
  - Reduced
  - Denied

Supported examples:
- Property damage claims  
- Fire and theft claims  
- Vehicle accident claims  
- Health insurance claims  

---

##  Output

A **customer-friendly claim explanation** containing:

- **Decision** – whether the claim was approved, reduced, or denied  
- **Covered Areas** – what parts of the claim are accepted  
- **Non-Covered Areas** – what is not included (if applicable)  
- **Reasoning** – simple explanation for the decision  
- **Tone** – polite, calm, and easy to understand  

---

##  Technology Used

- Python  
- Streamlit (UI)  
- Azure OpenAI (LLM)  
- LangChain (prompt control & response handling)  
- pdfplumber (PDF text extraction)  
- dotenv (environment configuration)  

---

##  How It Works

- Extracts text from the uploaded claim report PDF  
- Uses prompt engineering to control tone and clarity  
- Sends the claim content and decision to the AI model  
- Generates a clear and polite explanation in plain language  
- Displays the final explanation in a clean and professional UI  

---

##  How to Run

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add Azure OpenAI credentials in .env file

# Run the app
streamlit run app.py
