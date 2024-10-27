import os
import random
import time

import tweepy
from dotenv import load_dotenv
from post import create_post
from timezone import get_timezone

load_dotenv()

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
DEBUG = os.getenv("DEBUG")

client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET,
)

if __name__ == "__main__":
    delay = random.randint(0, 1800)  # Random delay (0-30 minutes)
    timezone = get_timezone()
    new_post = create_post(timezone)
    print(f"Posting: {new_post}\nDelay: {delay}s")
    if not DEBUG:
        time.sleep(delay)
        client.create_tweet(text=new_post)
