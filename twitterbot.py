from random import randrange
import twitter
import tweepy 
import time
while True:
	num1 = randrange(1,3435)
	num2 = randrange(3436,19155)

	f=open('geb.txt')
	lines=f.readlines()

	operator = randrange(0,1)

	if lines[num1].endswith(".") or lines[num1].endswith(","):
		line1 = lines[num1]
		line1.rsptrip()
		line1 = line1[:len(line1) - 1]
	else:
		line1 = lines[num1]

	if lines[num2].endswith(".") or lines[num2].endswith(","):
		line2 = lines[num2]
		line2.rstrip()
		line2 = line1[:len(line2) - 1]
	else:
		line2 = lines[num2]


	if operator == 0:
		tweet = line1.rstrip() + ' ' + line2
	else:
		tweet = line2.rstrip() + ' ' + line1

	print tweet
	
	try:
		twitterApi = twitter.Api(
		consumer_key = '##', 
		consumer_secret = '##', 
		access_token_key = '##',
		access_token_secret = '##')
		auth = tweepy.OAuthHandler('##', '##')
		auth.set_access_token('##', '##')
		tweepyApi = tweepy.API(auth)
		status = twitterApi.PostUpdate(tweet)
		print '  post successful!'
		for follower in tweepy.Cursor(tweepyApi.followers).items():
			follower.follow()
			print follower.screen_name

	except twitter.TwitterError:
		print 'error posting!'

	waittime = randrange(60, 1500)
	print waittime
	time.sleep(waittime)
