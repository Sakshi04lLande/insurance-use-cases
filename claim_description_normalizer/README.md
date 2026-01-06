# GenAI Claim Description Normalizer

## Project Overview

GenAI Claim Description Normalizer is a GenAI-based system that converts **raw insurance claim text**
into **structured and machine-readable data**.

Insurance companies receive claim information in free-text form such as emails, WhatsApp messages,
call center notes, and surveyor reports. These texts are often messy and hard to process automatically.

This project normalizes such unstructured claim descriptions into **clean structured data**
without guessing or making assumptions.

---

## Input

- Raw insurance claim description in **text format**
- Input can come from:
  - Customer emails
  - WhatsApp messages
  - Call center notes
  - Field surveyor / adjuster notes

Supported claim examples:
- Water damage claims  
- Fire and theft claims  
- Vehicle accident claims  
- Machinery and property damage claims  

---

## Output

The system generates **structured claim data** containing:

- **Loss Type** – type of incident (only if clearly mentioned)  
- **Severity** – impact level (Low / Medium / High) or `null` if unclear  
- **Affected Assets** – list of damaged or impacted items  
- **Incident Summary** – short factual summary of the claim  

The output is safe, clean, and ready to be used by insurance systems.

---

## Technology Used

- Python  
- Streamlit (User Interface)  
- Azure OpenAI (Large Language Model)  
- LangChain (prompt control and structured output)  
- Pydantic (schema validation)  
- dotenv (environment configuration)  

---

## How It Works

- User enters raw claim text in the application  
- AI reads and understands the claim description  
- Only **explicitly mentioned information** is extracted  
- No assumptions or guessing is done  
- Missing information is returned as `null`  
- Final structured output is displayed in the UI  

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

# Run the Streamlit app
streamlit run app.py
