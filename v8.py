import tweepy
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.
consumer_key="YSXHMWFQnu3GwhpIQzPxWQ"
consumer_secret="JoENQsyTtXOkP1UJHznDjSWPFcdgADZToFgHupKCjc"
access_token="1042496521-HfQSfLjfARBeE2TnvVL5W8ujrop9R3kAHC7GhI8"
access_token_secret="ypK48se8H1VX1q3GMQ0jo0VU5qNmUEmkGJC50CUk6PE"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
	
api = tweepy.API(auth)

string = "#Conclave13"

trend = api.search( string, result_type = "popular" )

i = 0
final = [[]]
jobj = {}

for t in trend:
	if i >= 3:
		break
	retweets = api.retweets(t.id_str, 100 )
	for tr in retweets:
		a = []
		a.append( tr.user.screen_name )
		
		if tr.user.location == "" and tr.user.time_zone == None: 
			continue
	
		elif tr.user.location == "" and tr.user.time_zone != None:
			
			jobj[tr.user.screen_name] = tr.user.time_zone
			a.append(tr.user.time_zone)
			final.append(a)

		elif tr.user.location != "":
			a.append(tr.user.location)
			jobj[tr.user.screen_name] = tr.user.location
			final.append(a)

	i = i + 1


for test in final:
	print test

names = jobj.viewkeys()	
places = jobj.viewvalues()
#for n in name:
#	print n

place = json.dumps( names )
name = json.dumps( places )	
	
	
