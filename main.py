from datetime import datetime
from zoneinfo import ZoneInfo
import socket
import psutil
import platform
import os
import requests
import flask
from flask import Flask, render_template, request, jsonify
import threading
import time

app = Flask(__name__)


# Basisinfos
short_day_name = datetime.today().strftime('%a')
full_day_name = datetime.today().strftime('%A')
time_today = datetime.today().strftime('%X')
date_today = datetime.today().strftime('%Y-%m-%d')
ip = socket.gethostbyname(socket.gethostname())
ram_use = psutil.virtual_memory().percent
cpu_temp = float(os.popen("vcgencmd measure_temp").readline().replace("temp=", "").replace("'C\n", "")) if platform.system() == "Linux" else 42.0

# OpenWeatherMap Einstellungen
API_KEY = "b069e8f69895792688c69e06c1380006"
LAT = 48.2092  # Ismaning Latitude
LON = 11.6633  # Ismaning Longitude
url = f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&exclude=minutely,hourly,alerts&units=metric&appid={API_KEY}"

# API-Abfrage mit Fehlerprüfung
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if 'current' in data:
        temp_now = data['current']['temp']
        weather_now = data['current']['weather'][0]['description']
        for day in data['daily']:
            dt = day['dt']  # UNIX Timestamp
            temp_day = day['temp']['day']
            weather_day = day['weather'][0]['description']
            date_str = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d')
            print(f"{date_str}: {temp_day}°C, {weather_day}")
    else:
        print("API-Antwort enthält kein Feld 'current'. Hier die Antwort:")
        print(data)
else:
    print(f"API-Anfrage fehlgeschlagen mit Statuscode: {response.status_code}")
    print("Antwort:", response.text)

# Uptime-Persistenz
UPTIME_FILE = 'uptime_save.txt'
try:
    with open(UPTIME_FILE, 'r') as f:
        saved_seconds = int(f.read().strip())
except Exception:
    saved_seconds = 0

uptime_start = time.time() - saved_seconds

def save_uptime_periodically():
    while True:
        current_uptime = int(time.time() - uptime_start)
        try:
            with open(UPTIME_FILE, 'w') as f:
                f.write(str(current_uptime))
        except Exception:
            pass
        time.sleep(1)

threading.Thread(target=save_uptime_periodically, daemon=True).start()

@app.route('/')
def index():
    return render_template("index.html",
                           short_day_name=short_day_name,
                           full_day_name=full_day_name,
                           time_today=time_today,
                           date_today=date_today,
                           ip=ip,
                           ram_use=ram_use,
                           cpu_temp=cpu_temp,
                           temp_now=temp_now if 'temp_now' in locals() else None,
                           weather_now=weather_now if 'weather_now' in locals() else None)

@app.route('/api/status')
def api_status():
    now = datetime.now()
    short_day_name = now.strftime('%a')
    full_day_name = now.strftime('%A')
    time_today = now.strftime('%X')
    date_today = now.strftime('%Y-%m-%d')
    ip = socket.gethostbyname(socket.gethostname())
    ram_use = psutil.virtual_memory().percent
    cpu_temp = float(os.popen("vcgencmd measure_temp").readline().replace("temp=", "").replace("'C\n", "")) if platform.system() == "Linux" else 42.0
    # Persistente Uptime
    uptime_seconds = int(time.time() - uptime_start)
    days = uptime_seconds // 86400
    hours = (uptime_seconds % 86400) // 3600
    minutes = (uptime_seconds % 3600) // 60
    seconds = uptime_seconds % 60
    uptime_str = f"{days}d {hours:02}:{minutes:02}:{seconds:02}"
    return jsonify({
        'short_day_name': short_day_name,
        'full_day_name': full_day_name,
        'time_today': time_today,
        'date_today': date_today,
        'ip': ip,
        'ram_use': ram_use,
        'cpu_temp': cpu_temp,
        'uptime': uptime_str
    })

@app.route('/api/weather')
def api_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&units=metric&appid={API_KEY}"
    print('[DEBUG] Wetter-API-URL:', url)
    temp_now = None
    weather_now = None
    icon = None
    try:
        response = requests.get(url, timeout=5)
        print('[DEBUG] Wetter-API-Status:', response.status_code)
        print('[DEBUG] Wetter-API-Response:', response.text)
        if response.status_code == 200:
            data = response.json()
            temp_now = data['main']['temp']
            weather_now = data['weather'][0]['description']
            icon = data['weather'][0]['icon']
    except Exception as e:
        print('[DEBUG] Wetter-API-Exception:', e)
    return jsonify({
        'temp_now': temp_now,
        'weather_now': weather_now,
        'icon': icon
    })

@app.route('/api/weekweather')
def api_weekweather():
    url = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&daily=temperature_2m_max,temperature_2m_min,weathercode&timezone=Europe%2FBerlin&language=de"
    print('[DEBUG] Open-Meteo-URL:', url)
    try:
        response = requests.get(url, timeout=5)
        print('[DEBUG] Open-Meteo-Status:', response.status_code)
        print('[DEBUG] Open-Meteo-Response:', response.text)
        if response.status_code == 200:
            data = response.json()
            return jsonify(data['daily'])
    except Exception as e:
        print('[DEBUG] Open-Meteo-Exception:', e)
    return jsonify({'error': 'no data'})

if __name__ == "__main__":
    app.run(debug=True)