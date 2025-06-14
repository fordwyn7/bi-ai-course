import requests

API_KEY = "8161af331ca22b74ce59139a744dc0d0"
CITY = "Andijan"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    print("The weather in", CITY, "is:")
    print("Temperature:", data['main']['temp'], "°C")
    print("Humidity:", data['main']['humidity'], "%")
    print("Wind Speed:", data['wind']['speed'], "m/s")
else:
    print("Failed to retrieve weather data:", response.status_code)
