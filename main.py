import requests
import os
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
    "cnt": 4

}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

rain_codes = [item["weather"][0]["id"] for item in weather_data["list"]]
for condition_code in rain_codes:
    if condition_code < 700:
        print("Bring Umbrella")
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body="Bring Umbrella",
            from_="+14708028763",
            to="+18777804236",
        )
        print(message.status)
        break
