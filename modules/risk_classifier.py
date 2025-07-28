def classify_risks(ai_analysis):
    risks = []
    for line in ai_analysis.split("\n"):
        if any(keyword in line.lower() for keyword in ["spoofing", "tampering", "repudiation", "information disclosure", "denial of service", "elevation of privilege"]):
            risks.append({"category": "STRIDE", "description": line})
        elif any(keyword in line.lower() for keyword in ["injection", "broken authentication", "sensitive data exposure", "security misconfiguration"]):
            risks.append({"category": "OWASP", "description": line})
    return risks
