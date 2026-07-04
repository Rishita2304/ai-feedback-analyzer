import requests

from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.environ.get("GEMINI_API_KEY")
URL = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

response = requests.get(URL)
data = response.json()

with open("models_list.txt", "w") as f:
    for model in data.get("models", []):
        methods = model.get("supportedGenerationMethods", [])
        if "generateContent" in methods:
            f.write(model["name"] + "\n")

print("Done! Check models_list.txt in your folder.")