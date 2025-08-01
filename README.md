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
