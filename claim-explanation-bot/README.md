# A GenAI-based application that explains insurance claim settlement decisions to customers in simple and easy language.

This bot helps customers understand why their claim was approved, reduced, or denied, without using complex insurance or legal terms.


# The explanation is:

Simple

Polite

Easy to understand

Non-technical

## How It Works

User uploads a claim report PDF

User selects the claim decision

The system extracts text from the PDF

A carefully designed prompt is sent to the AI model

The AI generates a clear explanation for the customer

## Key Features

Explains claim decisions in simple language

Works with real claim report PDFs

Polite and customer-friendly tone

Clean and professional UI

Easy to extend for future use cases

## Technologies Used

Python

Streamlit – for UI

Azure OpenAI – for generating explanations

LangChain – for prompt handling

PDFPlumber – for PDF text extraction

## Project Structure
claim-explanation-bot/
│
├── app.py          # Streamlit UI
├── claim_bot.py    # GenAI logic
├── requirements.txt
├── .env

## Environment Variables

Create a .env file and add the following:

AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name
AZURE_OPENAI_API_VERSION=2024-02-01


Do not upload .env file to GitHub

 How to Run the Project
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

## Demo Input

Upload any insurance claim report PDF

Select decision:

Approved

Reduced

Denied

 ## Output

The system generates a customer-friendly explanation clearly stating:

What is covered

What is not covered (if any)

Why the final decision was made



