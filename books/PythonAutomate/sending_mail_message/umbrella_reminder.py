"""umbrella_reminder.py
오늘 우산을 챙겨야 하는 지 알려주는 프로그램
"""
import sys
import json
import requests
import smtplib
from datetime import datetime
from email.mime.text import MIMEText

from settings import GMAIL_ID, GMAIL_PW, API_KEY


# Context Manager 사용
class MailServer(object):
    def __init__(self, id, pw):
        print("Connect Gmail SMTP server")
        self.smtp_obj = smtplib.SMTP_SSL(host="smtp.gmail.com", port=465)
        print("Login...", end=" ")
        self.smtp_obj.login(id, pw)
        print(" Complete")

    def __enter__(self):
        return self.smtp_obj

    def __exit__(self, type, value, traceback):
        return self.smtp_obj.quit()


def get_datetime(unix_time: int) -> datetime:
    return datetime.utcfromtimestamp(unix_time)


def today_weather(lat: str, lon: str):
    url = "https://api.openweathermap.org/data/2.5/onecall"
    resp = requests.get(url, params={"lat": lat, "lon": lon, "appid": API_KEY})
    resp.raise_for_status()

    data = json.loads(resp.text)
    today = data["daily"][0]
    tomorrow = data["daily"][1]

    weather = {
        "today": today["weather"][0],
        "tomorrow": tomorrow["weather"][0],
    }

    return weather


if __name__ == "__main__":
    seoul = {
        "lat": "37.532600",
        "lon": "127.024612"
    }

    weather = today_weather(seoul["lat"], seoul["lon"])

    today = datetime.today().strftime("%Y년 %m월 %d일")
    msgs = []
    msgs.append(f"오늘 날씨: {weather['today']['main']}, 상세: {weather['today']['description']}")
    msgs.append(f"내일 날씨: {weather['tomorrow']['main']}, 상세: {weather['tomorrow']['description']}")

    # Mail Part
    sender = GMAIL_ID
    recipients = ["imdff0803@gmail.com"]

    mime_msg = MIMEText("\n".join(msgs))
    mime_msg["Subject"] = f"{today} 날씨 예보"
    mime_msg["From"] = sender
    mime_msg["To"] = ", ".join(recipients)

    with MailServer(GMAIL_ID, GMAIL_PW) as smtp_obj:
        smtp_obj.send_message(mime_msg)
