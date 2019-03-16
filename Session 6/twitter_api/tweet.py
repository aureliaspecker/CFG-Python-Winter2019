import tweepy

with open("credentials.txt", "r") as file: 
    consumer_key = file.readline().split()[2] 
    consumer_secret = file.readline().split()[2]
    access_token = file.readline().split()[2]
    access_token_secret = file.readline().split()[2]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets_from_timeline = api.home_timeline()
for tweet in tweets_from_timeline:
    print tweet.text

text = raw_input("What would you like to Tweet?")

post_tweet = api.update_status(text)