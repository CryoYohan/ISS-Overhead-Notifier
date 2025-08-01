import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

if response.status_code != 200:
    response.raise_for_status()

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
print(f"Current Location of the ISS:\nLongitude: {longitude}\nLatitude: {latitude}")