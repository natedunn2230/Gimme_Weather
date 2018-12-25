import requests
api_key = "27575f230fc1ccd442725df200e6b8c1"
api_url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=imperial&APPID={}"

def get_weather_data(lat, long):
    data = requests.get(api_url.format(lat, long, api_key))

    description = data.json()['weather'][0]['description']
    temperature = round(data.json()['main']['temp'])

    return {'description': description, 'temperature': temperature}

    
    