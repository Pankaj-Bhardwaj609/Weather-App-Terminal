# 🌦️ Terminal Weather Forecast App

A simple **terminal-based weather forecast application** built using **Python**.  
This app fetches **real-time weather data** for any city using the **WeatherAPI** and displays detailed information directly in the terminal.

---

## 🚀 Features

- 🌍 Get real-time weather for any city
- 🌡️ Displays temperature in Celsius
- ☁️ Shows weather condition (Clear, Cloudy, Rain, etc.)
- 🕒 Displays local time of the city
- 🔄 Shows last updated weather time
- 🔐 Secure API key handling using `.env` file
- 🔁 Option to check multiple cities without restarting the app

---

## 🛠️ Technologies Used

- Python
- `requests` (for API calls)
- `python-dotenv` (for environment variables)
- WeatherAPI (external weather data source)

---

## 📂 Project Structure

```
weather-app/
│
├── weather.py # Main application file
├── .env # API key (not pushed to GitHub)
├── .gitignore # Ignored files
└── README.md # Project documentation
```

---

## 🔑 API Setup

1. Create a free account at **https://www.weatherapi.com/**
2. Generate your API key
3. Create a `.env` file in the project root
4. Add your API key like this:

`API_KEY=your_api_key_here`

---

## 📦 Installation

1. Install required packages:
`pip install requests python-dotenv`
2. Download and Run the application in your Code Editor:
`python weather.py`

---

## 📌 Example Output

```
--------Weather Forecast for London--------

City: London
State: City of London, Greater London
Country: United Kingdom
Temperature: 18°C
Weather: Partly cloudy
Local Time: 2026-01-06 10:15
Last Updated: 2026-01-06 10:00
```

---

## ❌ Error Handling

- Invalid city names
- API errors
- Empty input handling via API response status

---

## 🧠 Future Improvements

- GUI version using Tkinter

## 📜 License

This project is open-source and free to use for learning purposes.
