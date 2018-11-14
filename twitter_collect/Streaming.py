from tweepy.streaming import StreamListener
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        if  str(status) == "420":
            print(status)
            print("You exceed a limited number of attempts to connect to the streaming API")
            return False
        else:
            return True

import tweepy
# We import our access keys:

# Consume:
CONSUMER_KEY    = 'n3TzRWLq74mSlHWhsKUeGaroi'
CONSUMER_SECRET = 'UOHHeW4qfyLlYmeS9GNTIjWzjgveBHbvmVhfRbiLMzqUcOlwdQ'

# Access:
ACCESS_TOKEN  = '1062273051461668864-YOHoDYqOP0EIZXOKHsjfwj1hnCsDRy'
ACCESS_SECRET = 'djmrDY1wONKbr5hOAq85RzbDyWULG40WfWcPisGVvQ1Yg'


def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py
    :return: the authentified API
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api



def collect_by_streaming():

    connexion = twitter_setup()
    listener = StdOutListener()
    stream=tweepy.Stream(auth = connexion.auth, listener=listener)
    stream.filter(track=['Emmanuel Macron'])

def get_candidate_queries(num_candidate, file_path):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    try:
        # TO COMPLETE
    except IOError:
        # TO COMPLETE

