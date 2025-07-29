import json
import xml.etree.ElementTree as ET

def parse_report(uploaded_file):
    content = uploaded_file.read().decode("utf-8")
    if uploaded_file.name.endswith(".json"):
        return json.loads(content)
    elif uploaded_file.name.endswith(".xml"):
        root = ET.fromstring(content)
        return {child.tag: child.text for child in root}
    else:
        return {"text": content}
