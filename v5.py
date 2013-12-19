import tweepy
import json

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="AfNqoV9Hypx2EAjDoCEPg"
consumer_secret="83ItJs7CSt7ubfofB3azmyTjWmozjSjSGI7yHY"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located 
# under "Your access token")
access_token="463735426-D5kEHY048URNmO4U0x5VBtDOcrrDZzwvrvEPopXl"
access_token_secret="6DPL4qU7egtdtyrbIDHJgASIhwpOvBzPmIkUHg8lacQ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
	
api = tweepy.API(auth)

#hardcoding th query for now	
string = "PallaviGudipati"
#searching the user
query = api.search_users(string)

#storing the first hit	
person = query[0]	

print person.screen_name

if person.location != "" and person.location != None:
	print person.location

elif person.time_zone != "" and person.time_zone != None:
	print person.time_zone	

#getting the timeline of person
timeline = api.user_timeline(person.screen_name)

#getting the first tweet not retweet	
for status in timeline:
	if status.text[0] != 'R' or status.text[1] != 'T':	
		tweet = status
		break

print tweet.text	
retweets = api.retweets(tweet.id_str, 100)		

final =  [[]]
i = 0 

jobj = {person.screen_name:tweet.text}

for trend in retweets:

#	if i >= 50:
#		break

	if trend.user.location == "" and trend.user.time_zone == None: 
		continue
		
	elif trend.user.location == "" and trend.user.time_zone != None:
		a = []
		a.append(trend.user.screen_name)
		jobj[trend.user.screen_name] = trend.user.time_zone
		a.append(trend.user.time_zone)
		final.append(a)
		i = i + 1
	
	elif trend.user.location != "":
		a = []
		a.append(trend.user.screen_name)
		a.append(trend.user.location)
		jobj[trend.user.screen_name] = trend.user.location
		final.append(a)
		i = i + 1

#for test in final:
#	print test

name = jobj.viewkeys()
place = jobj.viewvalues()

for n in name:
	print n

json.dumps(jobj)	
	
