
import os
import google.generativeai as genai

print("API KEY:", os.getenv("GOOGLE_API_KEY"))
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)


def analyze_report(report_data):
    prompt = f"Analizza questo report di sicurezza e identifica i rischi: {report_data}"
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text
