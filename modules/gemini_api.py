import os
import google.generativeai as genai

# Configura l'API con la chiave (puoi anche usare una variabile d'ambiente)
API_KEY = "AIzaSyCGBdbg8MdHor_qRubS7nQ11JJmajMecNk"
genai.configure(api_key=API_KEY)

def analyze_report(report_data):
    prompt = f"Analizza questo report di sicurezza e identifica i rischi: {report_data}"
    
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        print("❌ Errore durante l'analisi del report:")
        print(f"Tipo di errore: {type(e).__name__}")
        print(f"Messaggio: {e}")
        return "Errore durante l'analisi del report. Controlla la configurazione dell'API o il contenuto del report."
