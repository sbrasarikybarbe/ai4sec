import google.auth
import google.generativeai as genai

credentials, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/generative-language"])
genai.configure(credentials=credentials)

def analyze_report(report_data):
    prompt = f"Analizza questo report di sicurezza e identifica i rischi: {report_data}"
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text
