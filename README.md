# RetroDashboard

A beautiful, retro-inspired dashboard for your Raspberry Pi or any PC – perfect for fullscreen displays, info screens, or your personal smart mirror!

---

<img src="https://github.com/user-attachments/assets/0530f7f6-a15a-4be9-b07a-186cec6a47cd" width="300">


_A preview of the dashboard in action._

---

## 💡 Real-Life Use Cases
- **Dedicated Info Screen:** Mount a Raspberry Pi with a display in your office or workshop to show time, weather, and system stats at a glance.
- **Personal Dashboard:** Run it on a secondary monitor as your personal, retro-themed command center.
- **Retro Kiosk:** Use it as a cool, interactive display for an event or public space.

---

## ✨ Features
- **Live Clock** with an epic New Year countdown and firework effects.
- **Current Weather** powered by OpenWeatherMap.
- **7-Day Weather Forecast** from Open-Meteo (no registration required).
- **System Info**: CPU temperature, RAM usage, system uptime, and local IP address.
- **Scrolling Ticker** with fun facts, dynamic holiday messages, and more.
- **Fullscreen Mode** for an immersive, distraction-free experience.
- **Authentic Retro Design**: CRT glow, pixel fonts, and a classic green/amber color scheme.
- **Responsive Layout**: Looks great on any screen size.

---

## 🚀 Quickstart

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Start the application:**
    ```bash
    python main.py
    ```
3.  **Open in your browser:**
    Navigate to `http://127.0.0.1:5000` in your web browser.

---

## 🖥️ Usage
- **Go Fullscreen:** Click the `⛶ Fullscreen` button in the top-right corner.
- **Simulate New Year's Eve:** Press `Alt+Q+F` to trigger a full New Year countdown with fireworks and a special ticker message.
- **Ticker:** Enjoy random facts and dynamic messages like "Christmas is in X days!"

---

## ⚙️ Configuration
- **Location:** Change the `LAT` and `LON` variables in `main.py` to set your city for weather forecasts.
- **Custom Ticker:** Edit the `static/js/ticker_messages.js` file to add your own messages to the scrolling ticker.
- **Design:** Tweak `static/css/style.css` to change colors, fonts, and CRT effects.

---

## ❓ FAQ
- **Can I run this on Windows, Linux, or Raspberry Pi?**
  > Yes! It works on any system with Python 3.9+ and Flask.
- **Do I need an API key?**
  > No key is needed for the 7-day forecast (Open-Meteo). For current weather, you can optionally add a free key from OpenWeatherMap.
- **How do I add my own ticker messages?**
  > Simply edit the `static/js/ticker_messages.js` file and add your lines to the array.

---

## 🤝 Contributing
Pull requests and new ideas are always welcome! Feel free to fork the repository, make improvements, and submit a PR.

---

## 📜 License
This project is licensed under the MIT License.
