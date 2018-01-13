import tweepy, time, requests

# consumer and access information, removed for modesty
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

# only accepting json in response objects
HEADERS = {"Accept":"application/json"}

# authorize Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# access Twitter
api = tweepy.API(auth)

# get pseudorandom color from colr.org, get hex from that
color = requests.get("http://www.colr.org/json/color/random", headers=HEADERS)
hexID = color.json()["colors"][0]["hex"]

# what to post
feed = "Good morning from Color Bot! The color of the day is 0x{}!".format(hexID)

# try posting the tweet, unless there's an error
try:
	api.update_status(feed)
except tweepy.TweepError as err:
	print(err)

# sleep for a day
time.sleep(86400)

# Based on tutorial from http://www.codingdojo.com/blog/make-twitter-bot-10-minutes/
