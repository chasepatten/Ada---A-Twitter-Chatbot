import time
import datetime
import sys
import AuthTwitter
import AuthFile
import TweetFuncs

if __name__ == '__main__':
    # I keep my keys and tokens encrypted in a seperate file
    AuthFile.decrypt_file()
    all_keys = open('ada', 'r').read().splitlines()
    api_consumer_key = all_keys[0]
    api_consumer_secret_key = all_keys[1]
    api_access_token = all_keys[2]
    api_token_secret = all_keys[3]
    api_bearer_token = all_keys[4]
    # After reading all the keys and tokens and placing them in a list I then reencrypt the file
    AuthFile.encrypt_file()

    # Used to hold the accounts we will follow and retweet
    accounts = open('accounts', 'r').read().splitlines()

    # Used to hold the tweets we premade for the bot to post
    tweets = open('tweets', 'r').read().splitlines()

    # This is our Twitter API client. This is what we use to talk to Twitter
    client = AuthTwitter.create_client(api_bearer_token, api_consumer_key, api_consumer_secret_key, api_access_token,
                                       api_token_secret)

    # A basic menu used to issue commands to the bot as well as start is operational loop
    choice = ''
    while choice != '0':
        choice = input("Input Command: ")
        str(choice)
        if choice == '0':
            print("Bot terminating...")
            sys.exit()

    # Post a tweet
        if choice == '1':
            print("Posting a tweet...")
            print("What would you like the tweet to say?")
            text = input("Tweet: ")
            TweetFuncs.post_tweet(str(text), client)
            print("Returning to menu.")
            continue

    # Follow an account
        if choice == '2':
            print("Following...")
            print("Who are we following?")
            account = input("Account to follow: ")
            user_id = TweetFuncs.get_user_id(account, client)
            TweetFuncs.follow_account(user_id, client)
            print("Returning to menu.")
            continue

    # Search for a user's ID
        if choice == '3':
            print("User ID Search...")
            print("Whose User ID to Get?")
            input_id = input("User ID: ")
            user_id = TweetFuncs.get_user_id(input_id, client)
            print(f'User ID: {user_id} for account {input_id}')
            continue

    # Retweet a user's tweet identified by the tweet's id
        if choice == '4':
            print("Retweet beginning....")
            print("What user to retweet?")
            input_id = input("User ID: ")
            user_id = TweetFuncs.get_user_id(str(input_id), client)
            tweet_id = TweetFuncs.get_user_tweet(user_id, client)
            TweetFuncs.like_tweet(tweet_id, client)
            TweetFuncs.retweet(tweet_id, client)

    # This is our bots operational loop
        if choice == '5':
            counter = 0
            while counter != 5:
                text = tweets[counter]
                TweetFuncs.post_tweet(text, client)
                print("-Tweet Successful. Posted at: ", datetime.datetime.now())
                user_id = TweetFuncs.get_user_id(accounts[counter], client)
                print("-Get User ID Successful. Posted at: ", datetime.datetime.now())
                TweetFuncs.follow_account(user_id, client)
                print("-Account Followed Successfully. Posted at: ", datetime.datetime.now())

                tweets = TweetFuncs.get_user_tweet(user_id, client)
                print("-Get User Tweet Successfully. Posted at: ", datetime.datetime.now())
                TweetFuncs.retweet(tweets, client)
                print("-Retweet Successful", datetime.datetime.now())
                TweetFuncs.like_tweet(tweets, client)
                print("-Tweet Liked Successfully", datetime.datetime.now())


                counter += 1
                print("-Going into sleep mode for 4 hours.")
                time.sleep(14400)
            continue

    print("-Bot Terminated.")





