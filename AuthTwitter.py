import tweepy


# Create the client that authorizes you to use Twitter's API functions and endpoints
def create_client(bearer_token, consumer_key, consumer_secret_key, access_token, access_token_secret):
    auth = tweepy.Client(bearer_token, consumer_key, consumer_secret_key, access_token, access_token_secret,
                wait_on_rate_limit=True)
    print("-Client Created.")
    return auth
