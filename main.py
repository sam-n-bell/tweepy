import tweepy
from settings import BEARER_TOKEN

client = tweepy.StreamingClient(BEARER_TOKEN)
