# RetroDashboard

A beautiful, retro-inspired dashboard for Raspberry Pi (or any PC) – perfect for fullscreen displays, info screens, or your personal smart mirror!

---

## ✨ Features
- **Live Clock** with epic New Year countdown and effects
- **Current Weather** (OpenWeatherMap, no key required for Open-Meteo 7-day forecast)
- **7-Day Weather Forecast** (Open-Meteo, no registration needed)
- **System Info**: CPU temp, RAM usage, uptime, IP
- **Scrolling Ticker** with fun facts, dynamic holiday messages, and more
- **Fullscreen Mode** (toggle with button)
- **Retro Design**: CRT glow, pixel fonts, green/amber color scheme
- **New Year Special**: Automatic and simulated fireworks, countdown, and special ticker
- **Responsive**: Looks great on any screen size

---

## 🚀 Quickstart

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Start the app:**
   ```bash
   python main.py
   ```
3. **Open in your browser:**
   

---

## 🖥️ Usage
- **Fullscreen:** Click the ⛶ Fullscreen button (top right)
- **Simulate New Year:** Press `Alt+Q+F` for a full New Year countdown, fireworks, and ticker
- **Weather:** No API key needed for 7-day forecast (Open-Meteo)
- **Ticker:** Enjoy random facts, and sometimes dynamic messages like "Christmas is in X days!"

---

## 📸 Screenshots
> _Add your screenshots here!_

---

## ⚙️ Configuration
- **Location:** Change `LAT` and `LON` in `main.py` for your city
- **Weather API:** Uses OpenWeatherMap for current weather, Open-Meteo for 7-day forecast
- **Custom Ticker:** Edit `static/js/ticker_messages.js` for your own messages

---

## ❓ FAQ
- **Can I run this on Windows, Linux, or Raspberry Pi?**
  > Yes! Any system with Python 3.9+ and Flask will work.
- **Do I need an API key?**
  > No key needed for Open-Meteo 7-day forecast. For current weather, you can use OpenWeatherMap (free key, optional).
- **How do I add my own ticker messages?**
  > Edit `static/js/ticker_messages.js` and add your lines to the array.
- **How do I change the design?**
  > Tweak `static/css/style.css` for colors, fonts, and effects.

---

## 🤝 Contributing
Pull requests and ideas are welcome! Feel free to fork and improve.

---

## 📜 License
MIT
