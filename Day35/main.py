import requests
import os

api_key = os.environ.get("OWM_API_KEY")


from twilio.rest import Client

api_url = "https://api.openweathermap.org/data/2.5/weather"
account_sid= os.environ.get("ACCOUNT_SID")
auth_token= os.environ.get("AUTH_TOKEN")
weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
}

response = requests.get(api_url, params=weather_params)
weather_data= response.json()
print(response.json())
datapoint= (weather_data["weather"][0]["id"])
will_rain= False
if datapoint > 600 :
    will_rain= True

if will_rain:
    client= Client(account_sid,auth_token)
    message = client.messages \
        .create(
        body= "hye! it's going to rain today . Remember to bring an umbrella  ",
        from_="+16814446516",
        to= " 12312321321"
    )
print(message.status)