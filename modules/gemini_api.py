import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

def analyze_report(report_data):
    prompt = f"Analizza questo report di sicurezza e identifica i rischi: {report_data}"
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text
