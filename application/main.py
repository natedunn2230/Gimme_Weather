import WeatherUtility
import GeoUtility

lat, long = GeoUtility.find_coordinates("Tampa Bay Florida")

desc, temp, humidity, wind = WeatherUtility.get_weather_data(lat, long)
print("Description: {}".format(desc))
print("Temperature: {}".format(temp))
print("Humidity: {}".format(humidity))
print("Wind Speed: {}".format(wind))
