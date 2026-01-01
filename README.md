
## Insurance Use Cases

This repository contains a collection of **GenAI-powered insurance use cases** built to automate and simplify key insurance workflows.  
Each project focuses on a real-world insurance problem and demonstrates how **Large Language Models (LLMs)**, **RAG pipelines**, and **vector databases** can be used in practical enterprise scenarios.

The projects are implemented as **independent tools**, mostly with **Streamlit-based web interfaces**, and are easy to run and understand.

---

## What This Repository Covers

| Tool | Problem Solved | AI Approach |
|-----|---------------|------------|
| Policy Summary Assistant | Converts long policy documents into simple summaries | Document chunking + LLM summarization |
| Claim Description Normalizer | Transforms unstructured claim text into structured data | Prompt-based extraction |
| Quote Comparison Chatbot | Answers questions by comparing insurance plans | RAG with vector search |
| Underwriting Assistant | Helps analyze risk using underwriting guidelines | Multi-document analysis |
| Claim Explanation Bot | Explains claim decisions in simple language | LLM-based reasoning |

---

## Project Structure

```

insurance-use-cases/
│
├── claim-explanation-bot/          # Explains claim decisions
│   ├── app.py
│   ├── claim_bot.py
│   ├── data/
│   ├── README.md
│   └── requirements.txt
│
├── claim_description_normalizer/   # Normalizes claim descriptions
│   ├── app.py
│   ├── claim_normalizer/
│   ├── README.md
│   └── requirements.txt
│
├── policy_summary_assistant/       # Policy document summarization
│   ├── app.py
│   ├── summarizer/
│   ├── uploaded-pdfs/
│   ├── README.md
│   └── requirements.txt
│
├── quote-comparison-chatbot/       # Insurance quote comparison
│   ├── app.py
│   ├── rag_engine/
│   ├── quote-health-insurance-direct.pdf
│   ├── README.md
│   └── requirements.txt
│
├── underwriting-assistant/         # Underwriting risk analysis
│   ├── app.py
│   ├── underwriting_assistant/
│   ├── underwriting_guidlines/
│   ├── README.md
│   └── requirements.txt
│
├── .env                            # Environment variables (not committed)
├── .gitignore
└── README.md                       # Main repository README

````

---

## How to Set Up

### 1. Install dependencies
Each project has its own `requirements.txt`.

```bash
pip install -r requirements.txt
````

---

### 2. Configure environment variables

Create a `.env` file in the root folder and add your API keys if required.

Example:

```
OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=your_endpoint
```

---

## How to Run Any Project

1. Go to the project folder:

```bash
cd project-folder-name
```

2. (Optional but recommended) Create virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
streamlit run app.py
```

Each project also has its **own README** with more details.

---

## Technologies Used

* Python
* Streamlit
* Large Language Models (LLMs)
* Azure OpenAI / OpenAI API
* LangChain
* ChromaDB (Vector Database)
* RAG (Retrieval-Augmented Generation)
* PDF processing libraries

---

## Important Notes

* Each project works **independently**
* Vector databases are created only once where required
* `.env` and `venv` are excluded using `.gitignore`
* All paths are relative — run scripts from their project folders

---

## Purpose of This Repository

* Practice real-world **insurance GenAI use cases**
* Learn prompt engineering and RAG workflows
* Build interview-ready AI projects
* Demonstrate end-to-end AI application design

---

## License

This repository is created for **learning and demonstration purposes**.

```



Just tell me 👍
```
