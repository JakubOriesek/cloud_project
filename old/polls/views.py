#from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.http import JsonResponse
#from .api_test import get_air_qualit
from django.shortcuts import render



history = []

def index(request):
    url = "https://api.waqi.info/feed/bratislava/?token=demo"
    response = requests.get(url)
    data = response.json()

    aqi = data["data"]["aqi"]
    temperature = data["data"]["iaqi"]["t"]["v"]
    humidity = data["data"]["iaqi"]["h"]["v"]
    time = data["data"]["time"]["s"]

    entry = f"AQI: {aqi} | Temp: {temperature} deg C | Humidity: {humidity}% | Time: {time}"

    history.append(entry)

    text = "\n".join(history)

    resp = HttpResponse(text, content_type="text/plain")
    print(resp)
    resp["Refresh"] = "5"

    return resp