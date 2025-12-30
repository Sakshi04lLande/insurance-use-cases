import streamlit as st
import json
from claim_normalizer import normalize_claim_description


# ======================================================
# PAGE CONFIG
# ======================================================
st.set_page_config(
    page_title="AI Claim Normalizer",
    layout="centered"
)

# ======================================================
# UI
# ======================================================
st.title("📄 AI Claim Description Normalizer")
st.write(
    "Convert **raw insurance claim notes** into **clean structured data** using GenAI."
)

st.divider()

claim_text = st.text_area(
    "Enter Raw Claim Description",
    height=200,
    placeholder="Paste adjuster or customer claim notes here..."
)

if st.button("Normalize Claim"):
    if not claim_text.strip():
        st.warning("Please enter claim text.")
    else:
        with st.spinner("Analyzing claim..."):
            result = normalize_claim_description(claim_text)

        st.success("Structured Claim Data")
        st.json(result)

st.divider()

st.caption(
    "Powered by Azure OpenAI + HuggingFace Embeddings + ChromaDB"
)
