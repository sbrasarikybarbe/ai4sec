import streamlit as st
import os
from modules import parser, gemini_api, risk_classifier, mitigations, dashboard

st.set_page_config(page_title="AI4Sec", layout="wide")
st.title("🔐 AI4Sec – AI-powered Security Report Analyzer")

uploaded_file = st.file_uploader("Carica un report di sicurezza (JSON, XML, TXT)", type=["json", "xml", "txt"])
if uploaded_file:
    report_data = parser.parse_report(uploaded_file)
    st.success("API KEY:")
    st.success("Report caricato e analizzato.")
    st.success(os.getenv("GEMINI_API_KEY"))

    with st.spinner("Analisi AI in corso..."):
        ai_analysis = gemini_api.analyze_report(report_data)

    risks = risk_classifier.classify_risks(ai_analysis)
    mitigations_list = mitigations.suggest_mitigations(risks)

    dashboard.show_dashboard(risks, mitigations_list)
