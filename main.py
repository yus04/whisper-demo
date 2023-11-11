import requests

azure_openai_endpoint = "<AZURE_OPENAI_ENDPOINT>"
deployment_name = "<YOUR_DEPLOYMENT_NAME>"
api_version = "2023-09-01-preview"
azure_openai_key = "<AZURE_OPENAI_KEY>"
file_path = "./wikipediaOcelot.wav"

url = f"{azure_openai_endpoint}/openai/deployments/{deployment_name}/audio/transcriptions?api-version={api_version}"

headers = {
    "api-key": azure_openai_key,
}

files = {
    "file": (file_path, open(file_path, "rb")),
}

response = requests.post(url, headers=headers, files=files)

if response.status_code == 200:
    print("API call successful. Response:")
    print(response.json())
else:
    print(f"API call failed with status code {response.status_code}. Response:")
    print(response.text)