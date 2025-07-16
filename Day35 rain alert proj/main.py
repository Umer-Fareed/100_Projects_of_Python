import requests

from twilio.rest import Client
api_key = "1c63106d351d9e43d14964e570ee8df0"
api_url = "https://api.openweathermap.org/data/2.5/weather"
account_sid= "ACd049081bc2cd805207d812eb014bb626"
auth_token= "0f0601a735aed59ee103d9c39684742c"
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