import tweepy
from textblob import TextBlob
consumer_key = 'ONjVyxGciubzngbyFkEE5nfdP'
consumer_key_secret = 'J8vxHqGlvx6BAtgXNPk7FJXI5C8327LgmZjz3B2rWU3At3hTVC'
access_token = '1660808815-lOlQEPsZmsB7E0B3RUW9VeoJJedFhQyDywC2g3Z'
access_token_secret = 'Tkueok3eYkCYOFnQPlwXwDM9lgdB4gJuT1YIXUXfdLc5M'
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
public_tweets = api.search('Dogs')
for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	if analysis.sentiment[0]>0:
		print ('Positive')
	else:
		print ('Negative')
	print("")