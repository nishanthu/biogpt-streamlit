import json
import requests
API_URL = "https://api-inference.huggingface.co/models/microsoft/BioGPT-Large-PubMedQA"
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}
def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))
data = query("how to prevent type-2 diabetes")
data = query(data[0]['generated_text'])
data = query(data[0]['generated_text'])
data = query(data[0]['generated_text'])

print(data)
