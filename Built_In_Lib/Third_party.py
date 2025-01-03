import requests

response = requests.get("https://localhost:7238/api/Authors", verify=False)
print(response.json())