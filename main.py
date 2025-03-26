import requests
import os
from datetime import datetime

#user_api = os.getenv('current_weather_data')
location = input("Enter the city name: ")


complete_api_link = f"https://api.weatherapi.com/v1/current.json?key=87694896368d4cfc9d874338251703 &q={location}"
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
if 'error' in api_data:
   print(f"Invalid city: {location}.Please check you city name.")
else:
    try:
        temp_city = api_data['current']['temp_c']  # Temperature in Celsius
        weather_desc = api_data['current']['condition']['text']  # Weather description
        hmdt = api_data['current']['humidity']  # Humidity
        wind_spd = api_data['current']['wind_kph']  # Wind speed in km/h
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        # Display the weather information
        print("-------------------------------------------------------------")
        print(f"Weather Stats for - {location.upper()} || {date_time}")
        print("-------------------------------------------------------------")
        print(f"Current temperature is: {temp_city:.2f} °C")
        print(f"Current weather description: {weather_desc}")
        print(f"Current humidity: {hmdt} %")
        print(f"Current wind speed: {wind_spd} km/h")

    except KeyError:
        print(f"Error: Unable to retrieve complete weather data for {location}.")
