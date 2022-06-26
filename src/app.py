import os
import request 
import tweepy
import pandas as pd 
from dotenv import load_dotenv


# load the .env file variables
load_dotenv()

consumer_key = os.env.get("CONSUMER_KEY")
consumer_secret = os.env.get("CONSUMER_SECRET")
bearer_token= os.env.get("BEARER_TOKEN")

# Creando cliente de Twitter

client = tweepy.Client( bearer_token=bearer_token, 
                        consumer_key=consumer_key, 
                        consumer_secret=consumer_secret,
                        return_type = requests.Response,
                        wait_on_rate_limit=True)

# Definiendo el query para Tweeter

query = '#100daysofcode (pandas OR python) -is:retweet'      

tweets = client.search_recent_tweets(query=query, 
                                    tweet_fields=['author_id','created_at','lang'],
                                     max_results=100)







# your app code here

