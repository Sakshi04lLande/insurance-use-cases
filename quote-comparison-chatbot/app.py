import streamlit as st
from rag_engine import create_rag_pipeline

st.set_page_config(
    page_title="Insurance Quote Comparison Assistant",
    page_icon="🛡️"
)

st.title("🛡️ Insurance Quote Comparison Chatbot")
st.write(
    "Ask any question about the insurance quotes. "
    "The assistant compares plans and explains differences in simple terms."
)

@st.cache_resource
def load_chain():
    return create_rag_pipeline("Quote_Health_Insurance_direct.pdf")

qa_chain = load_chain()

question = st.text_input(
    "Ask a question (e.g., Compare these plans, Which is better, Explain deductible, etc.)"
)

if question:
    with st.spinner("Analyzing insurance quotes..."):
        answer = qa_chain.run(question)

        # 🔒 Guardrail: document-based disclaimer
        answer = (
            "Note: The following answer is based only on the information "
            "available in the provided document.\n\n"
            + answer
        )

    st.subheader("Answer")
    st.write(answer)

