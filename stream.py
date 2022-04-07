import tweepy

import constants
from settings import (
    API_KEY,
    API_KEY_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET,
BEARER_TOKEN
)

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


class Listener(tweepy.StreamingClient):

    def on_tweet(self, tweet):
        print(f'New tweet: {tweet}')

    def on_status(self, status):
        print(status)#.user.secreen_name + ": " + status.text)

    def on_request_error(self, status_code):
        if status_code == 429:
            print(f'rate limited')
        elif status_code == 401:
            print(f'auth error')
        else:
            print(f'Request error {status_code}')

    def on_exception(self, exception):
        print(f'oof, {exception}')

    def get_rule_list(self):
        rules = self.get_rules().data
        return rules if rules else []

    def print_rules(self):
        rules = self.get_rule_list()
        for r in rules:
            print(f'Rule id {r.id} | {r.value}')
        if not rules:
            print(f'no rules!')

    def remove_all_rules(self):
        rules = self.get_rule_list()
        try:
            rules_to_delete = [getattr(r, "id") for r in rules]
            if rules_to_delete:
                self.delete_rules(rules_to_delete)
            for r in rules_to_delete:
                print(f'Removed rule id {r}')
        except Exception as e:
            print(f'Failed to delete rules {e}')

    def on_disconnect(self):
        print(f'disconnected')

stream_tweet = Listener(BEARER_TOKEN)

stream_tweet.remove_all_rules()
new_rules = [
    # Below will work
    #tweepy.StreamRule(value="Halo (Infinite OR MCC OR Paramount) lang:en -is:retweet -is:reply", tag="Halo")
    tweepy.StreamRule(value="Lightning (Ford OR F150 OR F-150 OR EV) lang:en -is:retweet -is:reply", tag="Ford EV"),
    tweepy.StreamRule(value="Silverado EV lang:en -is:retweet -is:reply", tag="Chevy EV")
]
stream_tweet.add_rules(new_rules)
stream_tweet.filter()
