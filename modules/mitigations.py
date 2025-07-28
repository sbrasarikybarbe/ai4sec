def suggest_mitigations(risks):
    suggestions = []
    for risk in risks:
        if "injection" in risk["description"].lower():
            suggestions.append("Usa query parametrizzate per prevenire SQL injection.")
        elif "spoofing" in risk["description"].lower():
            suggestions.append("Implementa autenticazione forte per prevenire spoofing.")
        else:
            suggestions.append("Applica controlli di sicurezza adeguati.")
    return suggestions
