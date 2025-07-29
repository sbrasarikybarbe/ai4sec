import streamlit as st
import google.generativeai as genai
import re
import pandas as pd

# Set up the page
st.set_page_config(page_title="AI4Sec Log Analyzer", layout="wide")
st.title("🔐 AI4Sec – AI-powered Log Analyzer")

# Upload log file
uploaded_file = st.file_uploader("Upload a system log file (.txt)", type=["txt"])

credentials, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/generative-language"])
genai.configure(credentials=credentials)

if uploaded_file:
    log_content = uploaded_file.read().decode("utf-8")
    st.success("Log file successfully loaded.")

    # Load prompt template
    with open("prompt.txt", "r") as f:
        prompt_template = f.read()

    # Replace placeholder with log content
    prompt = prompt_template.replace("{{CONTENT}}", log_content) + "\nRespond in English."

    # Run Gemini analysis
    with st.spinner("Analyzing log with Gemini..."):
        model = genai.GenerativeModel("gemini-2.5-flash-lite-preview-06-17")
        response = model.generate_content(prompt)
        analysis = response.text

    # Display raw AI output
    st.subheader("📋 AI Analysis Output")
    st.text_area("Raw Output", analysis, height=300)

    # Parse AI output into structured table
    pattern = r"Log:\s*(.*?)\n→ Anomaly:\s*(.*?)\n→ Category:\s*(.*?)\n→ Risk:\s*(.*?)\n→ Mitigation:\s*(.*?)(?=\nLog:|\Z)"
    matches = re.findall(pattern, analysis, re.DOTALL)

    if matches:
        data = []
        for log, anomaly, category, risk, mitigation in matches:
            data.append({
                "Anomaly": anomaly.strip(),
                "Log Reference": log.strip(),
                "Category": category.strip(),
                "Risk Level": risk.strip(),
                "Mitigation": mitigation.strip()
            })

        df = pd.DataFrame(data)
        st.subheader("📊 Detected Anomalies and Mitigations")
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("No structured anomalies found in the AI output.")
