import os

import requests

api_key = os.environ["API_KEY"]
response = requests.get(
    "https://api.openweathermap.org/data/2.5/onecall?lat=43.591290&lon=-79.650253&exclude=current,minutely,daily&appid=e93f6964ade3f8216a1942925dcc2068")
response.raise_for_status()

weather_data = response.json()
slice_object = slice(12)
twelve_hour_weather = []
for weather in range(13):
    twelve_hour_weather.append(weather_data['hourly'][weather]['weather'][0]['id'])

for weather in twelve_hour_weather:
    if weather < 700:
        print("Bring an umbrella")
        break
