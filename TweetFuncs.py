import tweepy


# Posts a tweet to the authenticated account which is passed by the api parameter
def post_tweet(tweet_text, api):
    api.create_tweet(text=tweet_text)
    print("-Tweet Posted!")


# Finds a user and follows them. Currently, from a premade list. Plan to upgrade where she makes her own choice.
def follow_account(account_id, api):
    api.follow_user(account_id)
    print("-Account successfully followed: " + str(account_id))


# Gets a specified user by screen name
def get_user_id(screen_name, api):
    user = api.get_user(username=screen_name)
    print("*" + screen_name + "*" + " successfully got.")
    user_id = str(user.data.id)
    return user_id


# Gets user's tweets as specified by the user's id
def get_user_tweet(user_id, api):
    tweets = api.get_users_tweets(id=user_id, max_results=5)
    ids = []

    for tweet in tweets.data:
        ids.append(str(tweet.id))

    id_to_pass = ids[0]

    return id_to_pass


# Function used to look people up
def retweet(tweet_id, api):
    api.retweet(tweet_id)
    print("-Retweet Successful.")


def like_tweet(tweet_id, api):
    api.like(tweet_id)
    print("-Tweet Liked.")
