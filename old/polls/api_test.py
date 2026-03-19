
'''
import requests
import time

def get_air_quality():
    url = "https://api.waqi.info/feed/bratislava/?token=demo"

    response = requests.get(url)
    data = response.json()

    aqi = data["data"]["aqi"]
    city = data["data"]["city"]["name"]

    return {
        "city": city,
        "aqi": aqi
    }


while True:
    url = "https://api.waqi.info/feed/bratislava/?token=demo"
    response = requests.get(url)
    data = response.json()

    aqi =  data["data"].get("aqi")
    Temp = data["data"]["iaqi"].get("t", {}).get("v")
    Hum =  data["data"]["iaqi"].get("h", {}).get("v")
    Time = data["data"]["time"]["s"]

    print("aqi:  ", aqi," Temperature: ",Temp,"Humidity:",Hum," Time: ",Time)
    time.sleep(5)
    '''