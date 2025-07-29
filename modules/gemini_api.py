import google.auth
import google.generativeai as genai

credentials, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/generative-language"])
genai.configure(credentials=credentials)

def analyze_report(report_data):
    with open("modules/prompt.txt", "r") as file:
        prompt_template = file.read()

    prompt = prompt_template.replace("{{CONTENT}}", str(report_data))

    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text
