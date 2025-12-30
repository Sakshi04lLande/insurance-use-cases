# Policy Summary Assistant

This project is a GenAI-based tool that reads long insurance policy PDFs and generates a clear, plain-language summary.

It extracts only factual information from the document and creates a structured summary covering:
Scope, Coverage, Exclusions, Limits & Conditions, and Missing Information.

The summary is limited to 200–300 words, avoids assumptions, and uses cautious language.
Built using Python, Streamlit, LangChain, and Azure OpenAI.

-Designed for insurance policy documents (health, group, endorsements, etc.)


## How to run the project

```bash
pip install -r requirements.txt
streamlit run app.py