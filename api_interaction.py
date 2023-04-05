import requests
import json

def get_chatgpt_api_key():
    return input("Please enter your openAI API key: ")

def send_request_to_chatgpt(api_key, file_list):
    url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "prompt": "Analyze the following Python files and generate a README.md and a user-friendly documentation.md:",
        "files": [{"name": file["name"], "content": file["content"]} for file in file_list],
        "max_tokens": 2048
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code != 200:
        raise Exception(f"ChatGPT API request failed with status code {response.status_code} and message {response.text}")

    result = json.loads(response.text)
    return {"readme": result["choices"][0]["text"], "documentation": result["choices"][1]["text"]}
