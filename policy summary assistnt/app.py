import streamlit as st
from summarizer import generate_policy_summary

st.set_page_config(page_title="Policy Summary Assistant", layout="wide")
st.title("📄 Policy Summary Assistant")

uploaded_file = st.file_uploader("Upload Policy PDF", type=["pdf"])

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Analyzing policy document..."):
        summary = generate_policy_summary("temp.pdf")

    st.markdown("## ✅ Policy Summary")
    st.write(summary)
