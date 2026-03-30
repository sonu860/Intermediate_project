import requests
def get_weather(city):
  
  base_url = "http://api.openweathermap.org/data/2.5/weather"
  params = {
          "q": city,
          "appid": "b40b00b3c851b876a2f25780045238fb",
          "units": "metric"  # Celsius
      }
      
  response = requests.get(base_url, params=params)
  data = response.json()
  city = data["name"]
  temp = data["main"]["temp"]
  feels_like = data["main"]["feels_like"]
  humidity = data["main"]["humidity"]
  weather_desc = data["weather"][0]["description"]
  wind_speed = data["wind"]["speed"]

  print("\n" + "="*40)
  print(f"🌍 Weather in {city}")
  print("="*40)
  print(f"🌡️ Temperature: {temp}°C (Feels like {feels_like}°C)")
  print(f"💧 Humidity: {humidity}%")
  print(f"🌬️ Wind Speed: {wind_speed} m/s")
  print(f"☁️ Condition: {weather_desc.capitalize()}")
  print("="*40)



def main():
    print("🌦️ Weather App")
    API_KEY = "your_api_key_here"   # 🔑 Yahan apna API key daalo
    
    while True:
        city = input("\nEnter city name (or 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("👋 Goodbye!")
            break
        if not city:
            print("Please enter a city name.")
            continue
        get_weather(city)

if __name__ == "__main__":
    main() 