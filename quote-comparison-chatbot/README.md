# Insurance Quote Comparison Assistant

This project is a GenAI-based assistant that reads health insurance quote PDFs and helps users compare policies before buying insurance.

It analyzes coverage details such as hospitalisation, surgery, limits, co-payments, and waiting periods, and then recommends the most suitable plan based on the user’s need (for example, future medical treatment or family coverage).

The assistant uses a document-grounded RAG approach, meaning all answers are generated strictly from the PDF content without assumptions or hallucinations.  
Responses are short, clear, and decision-focused.

Built using Python, LangChain, ChromaDB, and Azure OpenAI.

- Works on real insurance quote PDFs  
- Compares multiple plans from the same document  
- Explains coverage differences in simple language  
- Designed for learning, demos, and interview projects  

---

## How to run the project

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
