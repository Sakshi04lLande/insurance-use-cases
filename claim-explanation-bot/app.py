import streamlit as st
import tempfile
from claim_bot import explain_claim

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="GenAI Claim Explanation Bot",
    page_icon="📄",
    layout="wide"
)

# =====================================================
# HEADER
# =====================================================
st.markdown(
    """
    <h1 style="text-align:center;">📄 GenAI Claim Explanation Bot</h1>
    <p style="text-align:center; color:grey; font-size:16px;">
        Explain claim settlement decisions in simple, customer-friendly language
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# =====================================================
# MAIN LAYOUT
# =====================================================
left_col, right_col = st.columns([1, 1])

# =====================================================
# LEFT: INPUT SECTION
# =====================================================
with left_col:
    st.markdown("### 🧾 Claim Input")

    uploaded_pdf = st.file_uploader(
        "Upload Claim Report (PDF)",
        type=["pdf"],
        help="Upload the internal claim report document"
    )

    decision = st.selectbox(
        "Claim Decision",
        ["Approved", "Reduced", "Denied"],
        help="Select the final settlement decision"
    )

    generate_btn = st.button("🚀 Generate Explanation", use_container_width=True)

# =====================================================
# RIGHT: OUTPUT SECTION
# =====================================================
with right_col:
    st.markdown("### 🧠 Customer Explanation")

    if generate_btn:
        if not uploaded_pdf:
            st.warning("⚠️ Please upload a claim report PDF.")
        else:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_pdf.read())
                pdf_path = tmp.name

            with st.spinner("Analyzing claim and generating explanation..."):
                explanation = explain_claim(pdf_path, decision)

            st.success("✅ Explanation Generated Successfully")
            st.markdown(
                f"""
                <div style="
                    background-color:#f9f9f9;
                    padding:20px;
                    border-radius:10px;
                    border-left:6px solid #4CAF50;
                    font-size:16px;
                ">
                    <p style="color:#000000; margin:0;">
                       {explanation}
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

# =====================================================
# FOOTER
# =====================================================
st.markdown(
    """
    <hr>
    <p style="text-align:center; color:grey; font-size:13px;">
        Built using Azure OpenAI • Prompt Engineering • Streamlit
    </p>
    """,
    unsafe_allow_html=True
)
