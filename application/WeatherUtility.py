import requests
import GeoUtility

api_key = "27575f230fc1ccd442725df200e6b8c1"
api_url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=imperial&APPID={}"

def get_weather_data(addr):
    addr_lat, addr_long = GeoUtility.find_coordinates(addr)
    data = requests.get(api_url.format(addr_lat, addr_long, api_key)).json()

    description = data['weather'][0]['description']
    temperature = round(data['main']['temp'])
    humidity = round(data['main']['humidity'])
    wind_speed = round(data['wind']['speed'])

    return (description, temperature, humidity, wind_speed)

    
    
