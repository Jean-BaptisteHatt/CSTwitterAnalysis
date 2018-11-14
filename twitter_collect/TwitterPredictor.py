import tweepy

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
# Twitter App access keys for @user

# Consume:
CONSUMER_KEY    = 'n3TzRWLq74mSlHWhsKUeGaroi'
CONSUMER_SECRET = 'UOHHeW4qfyLlYmeS9GNTIjWzjgveBHbvmVhfRbiLMzqUcOlwdQ'

# Access:
ACCESS_TOKEN  = '1062273051461668864-YOHoDYqOP0EIZXOKHsjfwj1hnCsDRy'
ACCESS_SECRET = 'djmrDY1wONKbr5hOAq85RzbDyWULG40WfWcPisGVvQ1Yg'

def collect():
    connexion = twitter_setup()
    tweets = connexion.search("EmmanuelMacron",language="french",rpp=100)
    for tweet in tweets:
        print(tweet.text)

collect()
