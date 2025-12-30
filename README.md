#  Insurance Use Cases – GenAI Projects

This repository contains **multiple AI-driven insurance use cases** developed using **Generative AI, prompt engineering, and data analytics concepts**.  
Each project is stored in a **separate folder** and focuses on solving a **specific insurance business problem**.

---

##  Repository Structure
insurance-use-cases/
│
├── claim_description_normalizer/
│ ├── app.py
│ ├── claim_normalizer/
│ ├── README.md
│ └── requirements.txt
│
├── policy_summary_assistant/
│ ├── uploaded-pdfs/
│ ├── app.py
│ ├── summarizer/
│ ├── README.md
│ └── requirements.txt
│
├── quote-comparision-chatbot/
│ ├── app.py
│ ├── quote-health-insurance-direct.pdf
│ ├── rag_engine/
│ ├── README.md
│ └── requirements.txt
│
├── underwriting-assistant/
│ ├── app.py
│ ├── underwriting_assistant/
│ ├── underwriting_guidlines/
│ ├── README.md
│ └── requirements.txt
│
├── .env
├── .gitignore
└── README.md <-- (This file)

##  How to Run Any Project

1. Navigate to the project folder:
```bash

# Create virtual environment:

python -m venv venv


# Activate virtual environment:

venv\Scripts\activate


# Install dependencies:

pip install -r requirements.txt


# Run the app:

python app.py


(Refer to the individual project README for specific instructions.)

# Environment Variables

projects require API keys or environment variables.

Add them in the .env file

.env is ignored using .gitignore for security
