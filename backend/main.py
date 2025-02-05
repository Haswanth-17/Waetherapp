from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any frontend
    allow_methods=["GET"],
    allow_headers=["*"],
)

# OpenWeatherMap API Key (Get yours from https://openweathermap.org/api)
API_KEY = "01c882e18eda31694b49a3b6c1cb31c9"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.get("/weather")
def get_weather(city: str):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"]
        }
    else:
        return {"error": "City not found"}
