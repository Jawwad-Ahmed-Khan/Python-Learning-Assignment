import requests
from pprint import pprint

API_Key = '8276b457f7a264b0ea1f551ec87c89d8'
city = input("Enter the city name: ")
base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}"

weather_data = requests.get(base_url).json()
pprint(weather_data)
