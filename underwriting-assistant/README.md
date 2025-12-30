# GenAI Underwriting Assistant

This project is a GenAI-based underwriting assistant that helps assess insurance risk for applicants.  
The system reads underwriting guidelines from documents and uses an LLM to generate risk decisions.
Built using Python, Streamlit, LangChain, and Azure OpenAI.

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

This will open the Streamlit UI in your browser where you can enter applicant details and get an underwriting decision.
