import requests
import json
from datetime import datetime

class WeatherApi:
    def __init__(self, api_key):
        self.api_key = api_key
        self.file_name = 'weather.json'

    def save_file(self, weather_info):
        """Save only selected weather fields to JSON file."""
        try:
            with open(self.file_name, 'r') as f:
                existing_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []

        existing_data.append(weather_info)
        with open(self.file_name, 'w') as f:
            json.dump(existing_data, f, indent=4)
        print("✅ Data saved successfully!")

    def get_weather(self, city):
        """Fetch weather data and return only required fields."""
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()

            # Extract only required fields
            weather_info = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"],
                "wind_speed": data["wind"]["speed"],
                "timestamp": datetime.now().isoformat()  # optional: when fetched
            }
            return weather_info
        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 401:
                print("❌ Invalid API key.")
            elif response.status_code == 404:
                print(f"❌ City '{city}' not found.")
            else:
                print(f"HTTP error: {http_err}")
        except Exception as e:
            print(f"❌ Error: {e}")
        return None

def main():
    print("🌦️ Weather App")
    API_KEY = "b40b00b3c851b876a2f25780045238fb"  # Replace with your actual API key
    weather_app = WeatherApi(API_KEY)

    while True:
        city = input("\nEnter city name (or 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("👋 Goodbye!")
            break
        if not city:
            print("Please enter a city name.")
            continue

        weather_info = weather_app.get_weather(city)
        if weather_info is None:
            continue

        # Display
        print("\n" + "="*40)
        print(f"🌍 Weather in {weather_info['city']}")
        print("="*40)
        print(f"🌡️ Temperature: {weather_info['temperature']}°C (Feels like {weather_info['feels_like']}°C)")
        print(f"💧 Humidity: {weather_info['humidity']}%")
        print(f"🌬️ Wind Speed: {weather_info['wind_speed']} m/s")
        print(f"☁️ Condition: {weather_info['description'].capitalize()}")
        print("="*40)

        # Save only the required fields
        weather_app.save_file(weather_info)

if __name__ == "__main__":
    main()