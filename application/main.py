import WeatherUtility
from TwitterUtility import TwitterUtility
import time

if __name__ == "__main__":
    tweeter = TwitterUtility()
    while True:
        test_type = input('(1) Tweet Weather Data\n(2) Get Mentions\n')
        if test_type == "1":
            addr = input("Enter Address for weather data: ")
            description, temperature, humidity, wind = WeatherUtility.get_weather_data(addr)
            tweet = "WEATHER FOR {} (as of {})\n{}\n{}°F\n{}% humidity\n{} MPH winds".format(addr.upper(), time.strftime("%Y-%m-%d %H:%M"), description, temperature, humidity, wind)
            print(tweet)
            tweeter.post_tweet(tweet)
        elif test_type == "2":
            print(tweeter.get_mentions())
