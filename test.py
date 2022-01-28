from flask import Flask,render_template
from datetime import datetime
import os
import requests


app=Flask(__name__)

@app.route("/")
def index():
    # api= os.getenv("key")
    key = "472b405b8273df734d1dafb5b6d9cc2e"
    # location = input("enter city name:")
    location="Kasganj"
    api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location.lower()}&appid={key}"
    link = requests.get(api_link)
    api_data = link.json()

    temp = round((api_data['main']['temp']-273.15),2)
    description = api_data['weather'][0]['description']
    humidity = api_data['main']['humidity']
    wind_speed = api_data['wind']['speed']
    feels_like = round((api_data['main']['feels_like']-273.15),2)
    # date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
    info={"location":location,"temperature":temp,"description":description,"humidity":humidity,"wind_speed":wind_speed,"feels_like":feels_like}
    return render_template("index.html",info=info)

