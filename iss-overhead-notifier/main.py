import requests
from datetime import datetime
from time import sleep
import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

MY_LAT = 10.315699
MY_LNG = 123.885437
time_now = datetime.now()
sender_email = os.getenv("sender_email")
receiver_email = os.getenv("receiver_email")
password = os.getenv("PASSWORD")

def send_email():
    body = (
        "Hi there!\n\n"
        "Heads up — literally! 🌌\n"
        "The International Space Station (ISS) is currently passing right above your location, "
        "and it’s night time, which means you have a clear chance to spot it streaking across the sky.\n\n"
        "Step outside, look up, and enjoy this rare celestial sight! "
        "It’ll appear as a bright, fast-moving star silently gliding across the sky — no telescope needed.\n\n"
        "🕒 Don't miss it — this overhead pass only lasts a few minutes!\n\n"
        "Happy skywatching!\n"
        "— Your ISS Overhead Notifier"
    )

    msg = MIMEText(f"{body}")
    msg["Subject"] = "🚀 The ISS is Above You! Go Outside and Look Up!"
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()
            server.starttls()
            server.login(user=sender_email, password=password)
            server.sendmail(sender_email, receiver_email,msg.as_string())
            server.ehlo()
    except Exception as e:
        print("Error:", e)

def get_iss_location_api_data()->tuple:
    """
        Fetch ISS Location data from API
    """
    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
    except requests.exceptions.ConnectTimeout:
        print("Connection timeout, took too long to respond. Probably internet issues")
        return ()
    else:
        if response.status_code != 200:
            print(f"HTTP Error: {response.status_code}")
            return ()

        data = response.json()

        latitude = data["iss_position"]["latitude"]
        longitude = data["iss_position"]["longitude"]

        print(f"ISS Current Location: {latitude, longitude}\nMy Current Location: {(MY_LAT, MY_LNG)}")

        return latitude, longitude


def get_sunrise_sunset_data_api()->dict:
    """
        Fetch Sunrise Sunset Data from API
    """
    parameters = { # Parameters for Sunrise-Sunset API that requires your current Latitude and Longitude
        "lat": MY_LAT, # Latitude
        "lng": MY_LNG, # Longitude
        "formatted": 0, # Formatted off for 24-hour format
        "tzid": "Asia/Singapore" # For UTC +8 timezone
    }
    try:
        response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    except requests.exceptions.ConnectTimeout:
        print("Connection timeout, took too long to respond. Probably internet issues")
    else:
        if response.status_code != 200:
            print(f"HTTP Error: {response.status_code}")
            return {}

        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        print(f"Sunrise-Sunset API Time in 24-Hour Format:\nSunrise: {sunrise} Sunset: {sunset}")
        return {
            "sunrise": sunrise,
            "sunset": sunset
        }

if __name__ == "__main__":
    # These are constant data, no need to refetch
    sunrise_sunset = get_sunrise_sunset_data_api()
    sunrise = sunrise_sunset.get("sunrise")
    sunset = sunrise_sunset.get("sunset")

    while True:
        # Always call these functions to refetch new data from ISS location
        iss_location = get_iss_location_api_data()
        my_location = (MY_LAT, MY_LNG)# For testing, change this to => iss_location

        if iss_location == my_location:
            print("The ISS is above you!")
            if sunrise <= time_now.hour < sunset:
                print("Too bad the sun is up")
            else:
                print("Go outside and look up!")
                send_email() # Send email
        else:
            print("The ISS cannot be seen on where you at right now")

        print("Next scan in 60 seconds...")
        sleep(60)


