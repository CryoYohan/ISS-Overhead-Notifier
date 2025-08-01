# 🌌 ISS Overhead Notifier

A Python-based notifier that alerts you via email when the **International Space Station (ISS)** is passing directly overhead **during nighttime** at your current location.  
Perfect for skywatchers who don’t want to miss a rare glimpse of the ISS!

---

## 🚀 Features

- Tracks the ISS in real time using the [Open Notify API](http://open-notify.org/Open-Notify-API/ISS-Location-Now/).
- Fetches your local **sunrise and sunset** times using the [Sunrise-Sunset API](https://sunrise-sunset.org/api).
- Compares your location, ISS position, and the time of day.
- Sends you an email notification when the ISS is visible (overhead + nighttime).
- Fully automated – just run the script and let it notify you.

---

## 🧰 Requirements

- Python 3.x
- `requests`
- `smtplib` (built-in)
- `email` (built-in)

Install dependencies:

```bash
pip install requests
```

## 📦 How It Works

The script determines your current location via IP (optional: set coordinates manually).

It checks:

- ✅ Is the ISS currently above you?
- 🌙 Is it nighttime?

If **both conditions are met**, you receive an email with the subject:  
**🚀 The ISS is Above You! Go Outside and Look Up!**

---

## ✉️ Notification

Subject: 🚀 The ISS is Above You! Go Outside and Look Up!

Hi there!

Heads up — literally! 🌌
The International Space Station (ISS) is currently passing right above your location, and it’s night time, which means you have a clear chance to spot it streaking across the sky.

Step outside, look up, and enjoy this rare celestial sight!
It’ll appear as a bright, fast-moving star silently gliding across the sky — no telescope needed.

🕒 Don't miss it — this overhead pass only lasts a few minutes!

Happy skywatching!
— Your ISS Overhead Notifier


---

## ⚙️ Configuration

Make sure to set the following in your script:

- `sender_email`: Your email address
- `receiver_email`: Who should receive the alert
- `app_password`: Your Gmail app-specific password  
  *(Enable 2FA in your Google account and generate one under "App Passwords")*

---

## 🛰️ APIs Used

- [ISS Location API](http://open-notify.org/Open-Notify-API/ISS-Location-Now/)
- [Sunrise-Sunset API](https://sunrise-sunset.org/api)

---

## 🛡️ Disclaimer

- This tool relies on third-party APIs — ensure you handle API limits and error checking in production.
- Always keep your email credentials secure.  
  Use environment variables or a `.env` file instead of hardcoding.

---

## 📌 Author

Developed by **CryoYohan** — feel free to contribute or fork!



