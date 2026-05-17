import datetime

def get_weather_info(city):
    weather_data = {
        "New York":    {"temp": 72, "condition": "Sunny"},
        "London":      {"temp": 58, "condition": "Cloudy"},
        "Tokyo":       {"temp": 65, "condition": "Partly Cloudy"},
        "Addis Ababa": {"temp": 70, "condition": "Clear"},
        "Nairobi":     {"temp": 68, "condition": "Sunny"},
    }
    return weather_data.get(city, {"temp": "N/A", "condition": "Unknown"})

def main():
    print("===== Simple Weather App =====")
    print(f"Date: {datetime.date.today()}\n")
    cities = ["New York", "London", "Tokyo", "Addis Ababa", "Nairobi"]
    for city in cities:
        data = get_weather_info(city)
        print(f"{city}: {data['temp']}°F — {data['condition']}")

if __name__ == "__main__":
    main()
