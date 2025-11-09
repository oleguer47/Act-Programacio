import requests
import json

API_KEY = "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"

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

data = {
    "model": "gpt-3.5-turbo",  
    "messages": [
        {"role": "system", "content": "Eres un profesor."},
        {"role": "user", "content": "¿Quien es el mejor futbolista de la historia?"}
    ],
    "temperature": 0.7
}


response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    result = response.json()
    print(" Respuesta del modelo:")
    print(result["choices"][0]["message"]["content"])
else:
    print(" Error:", response.status_code)
    print(response.text)
