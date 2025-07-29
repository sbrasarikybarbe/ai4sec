import streamlit as st
import google.auth
import google.generativeai as genai
import re
import pandas as pd

# Set up the page
st.set_page_config(page_title="AI4Sec Log Analyzer", layout="wide")
st.title("🔐 AI4Sec – AI-powered Log Analyzer")

# Upload log file
uploaded_file = st.file_uploader("Upload a system log file (.txt)", type=["txt"])

# Authenticate with Google
try:
    credentials, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/generative-language"])
    genai.configure(credentials=credentials)
except Exception as e:
    st.error(f"Authentication failed: {e}")
    st.stop()

if uploaded_file:
    log_content = uploaded_file.read().decode("utf-8")
    if len(log_content.strip()) < 50:
        st.warning("The uploaded log file seems too short or empty. Please provide a valid log.")
        st.stop()

    st.success("Log file successfully loaded.")

    # Load prompt template
    try:
        with open("prompt.txt", "r") as f:
            prompt_template = f.read()
    except FileNotFoundError:
        st.error("The prompt.txt file is missing. Please ensure it exists in the same directory.")
        st.stop()

    # Replace placeholder with log content
    prompt = prompt_template.replace("{{CONTENT}}", log_content) + "\nRespond in English."

    # Run Gemini analysis
    with st.spinner("Analyzing log with Gemini..."):
        try:
            model = genai.GenerativeModel("gemini-2.5-flash-lite-preview-06-17")
            response = model.generate_content(prompt)
            analysis = response.text
        except Exception as e:
            st.error(f"Gemini analysis failed: {e}")
            st.stop()

    # Display raw AI output
    st.subheader("📋 AI Analysis Output")
    st.text_area("Raw Output", analysis, height=300)

    # Parse AI output into structured table
    pattern = r"Threat Name:\s*(.*?)\n(?:→|->)\s*Technical Evidence:\s*(.*?)\n(?:→|->)\s*Suggested Mitigation:\s*(.*?)(?=\nThreat Name:|\Z)"
    matches = re.findall(pattern, analysis, re.DOTALL)

    if matches:
        data = []
        for name, evidence, mitigation in matches:
            data.append({
                "Threat Name": name.strip(),
                "Technical Evidence": evidence.strip(),
                "Suggested Mitigation": mitigation.strip()
            })

        df = pd.DataFrame(data)
        st.subheader("🛡️ Detected Threats and Mitigations")
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("No structured threats found in the AI output.")
