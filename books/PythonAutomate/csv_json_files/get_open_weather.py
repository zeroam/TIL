"""get_open_weather.py
현재 날씨데이터를 API를 통해 가져오기
"""
import sys
import json
import requests
from datetime import datetime
from pprint import pprint

from settings import API_KEY


def get_datetime(unix_time: int) -> datetime:
    return datetime.utcfromtimestamp(unix_time)

LOCATION = {
    "seoul": {
        "lat": "37.532600",
        "lon": "127.024612",
    }
}


if __name__ == "__main__":
    # 커맨드 라인 입력 (현재 seoul 만 가능)
    if len(sys.argv) != 2:
        print(f"Usage: {__file__} city_name")
        sys.exit(1)

    location = LOCATION[sys.argv[1].lower()]

    # Download the JSON data from OpenWeatherMap.org's API
    url = "https://api.openweathermap.org/data/2.5/onecall"
    resp = requests.get(url, params={"lat": location["lat"], "lon": location["lon"], "appid": API_KEY})
    resp.raise_for_status()

    # Load JSON data into a Python variable
    data = json.loads(resp.text)
    daily_data = data["daily"]

    for day in daily_data:
        print(f"{get_datetime(int(day['dt']))} >")
        print(f"  일출 시간: {get_datetime(int(day['sunrise']))}")
        print(f"  일몰 시간: {get_datetime(int(day['sunset']))}")

        temp = day["temp"]
        print(f"  온도: {temp}")

        feels_like = day["feels_like"]
        print(f"  체감 온도: {feels_like}")


        print(f"  기압: {day['pressure']} hPa")
        print(f"  습도: {day['humidity']} %")
        print(f"  풍속: {day['wind_speed']} metre/sec")
        print(f"  구름: {day['clouds']} %")

        wheather = day['weather'][0]
        print(f"  날씨: {wheather}")
        print()