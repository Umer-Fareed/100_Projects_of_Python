import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

