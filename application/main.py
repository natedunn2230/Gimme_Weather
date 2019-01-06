import WeatherUtility
from TwitterUtility import TwitterUtility

if __name__ == "__main__":
    while True:
        addr = input("Enter Address for weather data: ")
        description, temperature, humidity, wind = WeatherUtility.get_weather_data(addr)
        tweet = "WEATHER REPORT FOR {}:\n{}\n{}°F\n{}% humidity\n{} MPH winds".format(addr.upper(), description, temperature, humidity, wind)
        print(tweet)
        tweeter = TwitterUtility()
        tweeter.post_tweet(tweet)
