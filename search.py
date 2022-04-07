import tweepy
from settings import BEARER_TOKEN
from datetime import datetime, timedelta


class Search:

    def __init__(self, token):
        self.client = tweepy.Client(token)


    def search_recent_tweets(self, criteria, since):
        try:
            response = self.client.search_recent_tweets(query=criteria, start_time=since)
            results = response.data
            for r in results:
                print(r.text)
        except Exception as e:
            print(f'uh oh...{e}')


    def search_all_tweets(self, criteria):
        """
        only works for academic accounts
        :param criteria:
        :return:
        """
        try:
            response = self.client.search_all_tweets(query=criteria)
            results = response.data
            for r in results:
                print(r.text)
        except Exception as e:
            print(f'uh oh...{e}')


query = "Lightning (Ford OR F-150 OR F150) lang:en -is:retweet -is:reply"

searcher = Search(BEARER_TOKEN)
since = datetime.utcnow() - timedelta(hours=1)
searcher.search_recent_tweets(query, since)



