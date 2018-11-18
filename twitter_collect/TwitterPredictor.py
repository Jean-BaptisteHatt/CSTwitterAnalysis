import tweepy
import numpy as np

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

def collect_by_user(user_id):
    connexion = twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 1000)
    for status in statuses:
        print(status.text)
    return statuses

##collect_by_user(15251629)
collect()

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


rt_max  = np.max(data['RTs'])
rt  = data[data.RTs == rt_max].index[0]

# Max RTs:
print("The tweet with more retweets is: \n{}".format(data['tweet_textual_content'][rt]))
print("Number of retweets: {}".format(rt_max))
print("{} characters.\n".format(data['len'][rt]))



tfav = pd.Series(data=data['Likes'].values, index=data['Date'])
tret = pd.Series(data=data['RTs'].values, index=data['Date'])

# Likes vs retweets visualization:
tfav.plot(figsize=(16,4), label="Likes", legend=True)
tret.plot(figsize=(16,4), label="Retweets", legend=True)

plt.show()


print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data['tweet_textual_content'])))
print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(data['tweet_textual_content'])))
print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/len(data['tweet_textual_content'])))
