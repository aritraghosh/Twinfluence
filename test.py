import tweepy
import json
      
    consumer_key="YSXHMWFQnu3GwhpIQzPxWQ"
    consumer_secret="JoENQsyTtXOkP1UJHznDjSWPFcdgADZToFgHupKCjc"

		# The access tokens can be found on your applications's Details
		# page located at https://dev.twitter.com/apps (located 
		# under "Your access token")
    access_token="1042496521-HfQSfLjfARBeE2TnvVL5W8ujrop9R3kAHC7GhI8"
    access_token_secret="ypK48se8H1VX1q3GMQ0jo0VU5qNmUEmkGJC50CUk6PE"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#hardcoding th query for now	
#		string = "PallaviGudipati"
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

final = []
i = 0 

jobj = {'address':person.location}
#		jobj = {person.screen_name:tweet.text}

for trend in retweets:

#	if i >= 50:
#		break

if trend.user.location == "" and trend.user.time_zone == None: 
continue

elif trend.user.location == "" and trend.user.time_zone != None:
a = []
a.append('address')
#				jobj[trend.user.screen_name] = trend.user.time_zone
jobj['address'] = trend.user.time_zone
a.append(trend.user.time_zone)
#                array1.append(trend.user.time_zone)
final.append(trend.user.time_zone)
i = i + 1

elif trend.user.location != "":
a = []
a.append('address')
a.append(trend.user.location)
#				jobj[trend.user.screen_name] = trend.user.location
jobj['address'] = trend.user.location
final.append(trend.user.location)
#                array1.append(trend.user.location)
i = i + 1

#for test in final:
#	print test

#		name = jobj.viewkeys()
#		place = jobj.viewvalues()

#		for n in name:
#			print n

kolkata=json.dumps(final)	
		
