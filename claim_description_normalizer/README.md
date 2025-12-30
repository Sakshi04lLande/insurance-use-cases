# AI Claim Description Normalizer

## Project Overview

This project is an AI-based system that converts unstructured insurance claim text
into structured, machine-readable data.

Insurance companies receive claim information in free-text form such as:
- customer emails
- WhatsApp messages
- call center notes
- surveyor or adjuster reports

These texts are difficult to process automatically.  
This project solves that problem.

---

## What This Project Does

The system takes raw claim text as input and extracts:

- Loss Type  
- Severity (only if clearly mentioned, otherwise null)  
- Affected Assets  
- Incident Summary  

The output is clean and structured data that can be used by insurance systems.

## Create virtual environment

It is recommended to use a virtual environment.
```bash
python -m venv venv
venv\Scripts\activate
Install dependencies
pip install -r requirements.txt

## Environment variables

Create a .env file in the project root and add your Azure OpenAI details:

AZURE_OPENAI_ENDPOINT=your_endpoint
AZURE_OPENAI_DEPLOYMENT=your_deployment_name
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_VERSION=your_api_version

## Run the application
streamlit run app.py

