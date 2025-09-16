import requests

# URL of your Flask app
url = "http://127.0.0.1:5000/predict"

# Example input features
data = {
    "URL_Length": 120,
    "HTTPS": 0,
    "Subdomains": 1
}

response = requests.post(url, json=data)
print(response.json())
