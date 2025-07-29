# 🔐 AI4Sec – AI-powered Security Report Analyzer

**AI4Sec** is an interactive Streamlit application that leverages Google Gemini (Generative AI) to automatically analyze security reports, classify risks using STRIDE and OWASP Top 10 models, suggest mitigations, and visualize results through interactive dashboards.

## 🚀 Features

- 📄 Upload security reports in JSON, XML, or TXT format
- 🤖 Automatic analysis using Google Gemini API
- 🧠 Risk classification based on STRIDE and OWASP Top 10
- 🛡️ Mitigation suggestions for each identified risk
- 📊 Interactive dashboard with charts and tables

## 🧰 Requirements

- Python 3.10+
- Google Cloud Project with Gemini API enabled
- Proper authentication for `google-generativeai` (ADC or service account)

## 🧪 Run Locally

```bash
git clone https://github.com/sbrasarikybarbe/ai4sec.git
cd ai4sec
pip install -r requirements.txt
streamlit run app.py
