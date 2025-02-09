import typer
import time
from yaspin import yaspin
import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

def load_translation():
    lang = os.getenv("TOOL_LANGUAGE", "en")  

    try:
        with open(f"locales/{lang}.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Translation file for '{lang}' not found. Falling back to English.")
        with open("locales/en.json", "r", encoding="utf-8") as file:
            return json.load(file)

translations = load_translation()

spinner = yaspin()
spinner.start()

api_key=os.getenv('API_KEY')
lang = os.getenv('TOOL_LANGUAGE', 'en')

def weather(city: str):
    res = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&lang={lang}") 
    data = res.json()

    weather_data = {
        "name": data["location"]["name"],
        "region": data["location"]["region"],
        "country": data["location"]["country"],
        "lat": data["location"]["lat"],
        "lon": data["location"]["lon"],
        "localtime": data["location"]["localtime"],
        "temp": data["current"]["temp_c"],
        "feels_like": data["current"]["feelslike_c"],
        "condition": data["current"]["condition"]["text"],
        "humidity": data["current"]["humidity"],
        "pressure": data["current"]["pressure_mb"],
        "wind_speed": data["current"]["wind_kph"],
        "wind_dir": data["current"]["wind_dir"],
        "precipitation": data["current"]["precip_mm"],
        "uv_index": data["current"]["uv"]
    }

    print("\n")
    print(translations["weather-info"]["location"].format(**weather_data))
    print(translations["weather-info"]["localtime"].format(**weather_data))
    print(translations["weather-info"]["temperature"].format(**weather_data))
    print(translations["weather-info"]["condition"].format(**weather_data))
    print(translations["weather-info"]["humidity"].format(**weather_data))
    print(translations["weather-info"]["pressure"].format(**weather_data))
    print(translations["weather-info"]["wind"].format(**weather_data))
    print(translations["weather-info"]["precipitation"].format(**weather_data))
    print(translations["weather-info"]["uv"].format(**weather_data))
    print("\n")


if __name__ == "__main__":
    time.sleep(3)
    spinner.stop()
    typer.run(weather)