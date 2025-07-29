import google.auth
import google.generativeai as genai

credentials, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
genai.configure(credentials=credentials)

def analyze_report(report_data):
    prompt = f"Analizza questo report di sicurezza e identifica i rischi: {report_data}"
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text
