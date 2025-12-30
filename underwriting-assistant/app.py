import streamlit as st
from underwriting_assistant import underwriting_assistant

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="GenAI Underwriting Assistant",
    page_icon="🧠",
    layout="wide"
)

# =========================================================
# HEADER
# =========================================================
st.markdown(
    """
    <h1 style='text-align: center;'>🧠 GenAI Underwriting Assistant</h1>
    <p style='text-align: center; color: grey;'>
    AI-powered risk assessment for insurance underwriting
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# =========================================================
# MAIN LAYOUT
# =========================================================
left_col, right_col = st.columns([2, 1])

# =========================================================
# LEFT COLUMN – INPUT FORM
# =========================================================
with left_col:
    st.subheader("📋 Applicant Information")

    with st.container(border=True):
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=18, max_value=100)
        occupation = st.text_input("Occupation")
        annual_income = st.number_input("Annual Income (₹)", min_value=0, step=50000)
        credit_score = st.slider("Credit Score", 300, 900, 650)
        location_risk_zone = st.selectbox(
            "Location Risk Zone", ["Low", "Medium", "High"]
        )

    st.subheader("📑 Claims History")

    with st.container(border=True):
        has_claims = st.radio("Any previous claims?", ["No", "Yes"], horizontal=True)

        claims_history = []
        if has_claims == "Yes":
            claim_year = st.number_input("Claim Year", min_value=2000, max_value=2025)
            claim_amount = st.number_input("Claim Amount (₹)", min_value=0)
            claim_type = st.text_input("Claim Type")

            claims_history.append({
                "year": claim_year,
                "claim_amount": claim_amount,
                "claim_type": claim_type
            })

    st.subheader("🧪 External Risk Indicators")

    with st.container(border=True):
        fraud_flag = st.radio("Fraud Flag", [False, True], horizontal=True)
        medical_risk = st.selectbox("Medical Risk Level", ["Low", "Moderate", "High"])

    assess_btn = st.button("🔍 Assess Underwriting Risk", use_container_width=True)

# =========================================================
# RIGHT COLUMN – OUTPUT
# =========================================================
with right_col:
    st.subheader("📊 Underwriting Decision")

    if assess_btn:
        input_data = {
            "applicant": {
                "name": name,
                "age": age,
                "occupation": occupation,
                "annual_income": annual_income,
                "credit_score": credit_score,
                "location_risk_zone": location_risk_zone
            },
            "claims_history": claims_history,
            "external_reports": {
                "fraud_flag": fraud_flag,
                "medical_risk": medical_risk
            }
        }

        with st.spinner("Analyzing applicant risk..."):
            result = underwriting_assistant(input_data)

        decision = result.dict()

        # ===============================
        # RISK SCORE INDICATOR
        # ===============================
        risk_score = decision["risk_score"]

        if risk_score <= 40:
            st.success(f"🟢 Low Risk Applicant (Score: {risk_score})")
        elif risk_score <= 70:
            st.warning(f"🟠 Medium Risk Applicant (Score: {risk_score})")
        else:
            st.error(f"🔴 High Risk Applicant (Score: {risk_score})")

        # ===============================
        # PROFESSIONAL DECISION SUMMARY
        # ===============================
        st.markdown("### 📝 Decision Summary")

        with st.container(border=True):
            st.markdown(
                f"""
                **Risk Category:**  
                {decision['risk_category']}

                **Underwriting Recommendation:**  
                {decision['underwriting_recommendation']}

                **Underwriter’s Rationale:**  
                {decision['justification']}
                """
            )

        # ===============================
        # OPTIONAL TECHNICAL VIEW
        # ===============================
        with st.expander(" View Technical Output (Optional)"):
            st.json(decision)

    else:
        st.info("Fill applicant details and click **Assess Underwriting Risk**")
