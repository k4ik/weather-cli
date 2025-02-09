# 🌦️ Weather CLI 
[📜 English](README.md) | [📜 Português](README-PT.md)

Weather CLI is a simple command-line tool to get real-time weather information using the WeatherAPI. The project allows you to configure an API Key and select a language for data display.

![Demo](demo.gif)

## 📌 Features
- 🌎 Fetches weather information for any city
- 🌡️ Displays temperature, humidity, wind, pressure, and more
- 🌍 Supports multiple languages
- ⚙️ Easy setup via `setup.py`

## 🚀 Installation

### 1️⃣ Clone the repository:
```sh
git clone https://github.com/k4ik/weather-cli.git
cd weather-cli
```

### 2️⃣ Create a virtual environment (optional but recommended):
```sh
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

### 3️⃣ Install dependencies:
```sh
pip install -r requirements.txt
```

## ⚙️ Configuration
### 1️⃣ Set up API Key and language:
```sh
python setup.py
```
Follow the on-screen instructions to enter your WeatherAPI key and choose a language.

## 🌦️ How to Use
### 1️⃣ Get weather forecast for a city:
```sh
python weather.py [city_name]
```
Example:
```sh
python weather.py "New York"
```
Expected output:
```
📍 Location: New York, New York, USA (40.71, -74.01)
🕒 Local time: 2025-02-08 19:19
🌡️ Temperature: 12.3°C (Feels like: 10.0°C)
⛅ Condition: Cloudy
💧 Humidity: 75%
⚖️ Pressure: 1015.0 mb
💨 Wind: 15.0 km/h NW
🌧️ Precipitation: 0.0 mm
🔆 UV Index: 3.0
```

## 📜 License
This project is licensed under the MIT License.

