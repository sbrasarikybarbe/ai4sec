import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyCGBdbg8MdHor_qRubS7nQ11JJmajMecNk")

def analyze_report(report_data):
    prompt = f"Analizza questo report di sicurezza e identifica i rischi: {report_data}"
    model = genai.GenerativeModel("gemini-2.5-pro")
    response = model.generate_content(prompt)
    return response.text
