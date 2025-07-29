import streamlit as st
import parser, gemini_api, risk_classifier, mitigations, dashboard

st.set_page_config(page_title="AI4Sec", layout="wide")
st.title("🔐 AI4Sec – AI-powered Security Report Analyzer")

uploaded_file = st.file_uploader("Upload your log file (JSON, XML, TXT)", type=["json", "xml", "txt"])
if uploaded_file:
    report_data = parser.parse_report(uploaded_file)
    st.success("Report succesfully loaded.")

    with st.spinner("AI analysis running..."):
        ai_analysis = gemini_api.analyze_report(report_data)

    risks = risk_classifier.classify_risks(ai_analysis)
    mitigations_list = mitigations.suggest_mitigations(risks)

    dashboard.show_dashboard(risks, mitigations_list)
