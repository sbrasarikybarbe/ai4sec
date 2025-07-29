import json
import google.auth
import google.generativeai as genai

credentials, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/generative-language"])
genai.configure(credentials=credentials)

def analyze_report(report_data):
    with open("modules/prompt.txt", "r") as file:
        prompt_template = file.read()

    # Se è un dizionario (es. JSON), lo convertiamo in stringa formattata
    if isinstance(report_data, dict):
        content = json.dumps(report_data, indent=2)
    else:
        content = str(report_data)

    prompt = prompt_template.replace("{{CONTENT}}", content)

    model = genai.GenerativeModel("gemini-2.5-flash-lite-preview-06-17")
    response = model.generate_content(prompt)
    return response.text
