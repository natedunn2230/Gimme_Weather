import json
import tweepy

class TwitterUtility:
    def __init__(self):
        # Load config file
        self.key_file = open("../configure.json", "r")
        self.twitter_data = json.load(self.key_file)['TWITTER_API']

        # API Keys
        self.CONSUMER_KEY = self.twitter_data['CONSUMER_KEY']
        self.CONSUMER_SECRET = self.twitter_data['CONSUMER_SECRET']
        self.ACCESS_TOKEN = self.twitter_data['ACCESS_TOKEN']
        self.ACCESS_SECRET = self.twitter_data['ACCESS_SECRET']

        # Authenticate
        self.auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        self.auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_SECRET)
        
        #Twitter API
        self.twitter_api = tweepy.API(self.auth)

    def post_tweet(self, tweet):
        self.twitter_api.update_status(tweet)