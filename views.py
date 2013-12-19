from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import redirect,render
from django.utils import simplejson
import datetime
from django.template import RequestContext
from django.utils import simplejson
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
import tweepy
import json
def search(request):
    return render_to_response('test.html',locals(),context_instance=RequestContext(request))
def new(request):
    return render_to_response('srkv3.html',locals(),context_instance=RequestContext(request))
def form(request):
	
    if request.GET:
        return render_to_response('complete_signup2.html', locals(),context_instance=RequestContext(request))
        response_dict={}
        name = request.GET.get('username', False)
        response_dict.update({'name': name ,})
        if request.is_ajax():
            return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
    else:
        return render_to_response('complete_signup2.html', locals(),context_instance=RequestContext(request))
@csrf_exempt
def MyAjaxView(request):
    if request.is_ajax():
         if request.method == 'GET':
             print request.GET
         elif request.method == 'POST':
             print request.POST
    else:
        return render_to_response('hello.html', locals(), context_instance=RequestContext(request))
def qwerty(request):
    return render_to_response('qwerty.html',locals(),context_instance=RequestContext(request))
def donate(request):
    if request.method == 'POST':
        form = DonateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("SuccessFully Saved")
        else:
            return HttpResponse("Error in saving")
    return render_to_response('cry.html',locals(),context_instance=RequestContext(request))
def start(request):
    if request.method == 'POST':
    	
        string = request.POST.get('username', '')
#		name.append("pallavi")
#		simplejson.dumps(name)		
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
		
		
    return render_to_response('complete_signup3.html',locals(),context_instance=RequestContext(request))
def hacku(request):
    if request.method=='POST':
        string = request.POST.get('username', '')
        response_dict=[]
        response_dict.append("kolkata")
        response_dict.append("mumbai")
        response_dict.append("chennai")

#        response_dict.append({'address',"kolkata"})
#        response_dict.append({'address',"mumbai"})
       # response_dict.append[{"c",3}]
        jsondict=json.dumps(response_dict)           
    return render_to_response('wait.html',locals(),context_instance=RequestContext(request))
import tweepy
import json
def start2(request):
# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
    if request.method == 'POST':
        string = request.POST.get('username', '')
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

        # befor getting the first tweet not retweet
        # now getting the first five tweets	
        tweet = []      
        j = 0  
        for status in timeline:
            if status.text[0] != 'R' or status.text[1] != 'T':	
                tweet.append( status )
                j = j + 1
            if j >= 5:
                break

#        print tweet.text	
 
		

        final =  [[]]
        array = []
        arraynames = []
        i = 0 

        jobj = {}

        for tw in tweet:

            retweets = api.retweets(tw.id_str, 100)

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
        places=[]
        names = []
        for k in place:
            places.append(k)       
        for n in name:
            names.append(n)
            
        response_dict=json.dumps(places);
        naam=json.dumps(names);


    return render_to_response('complete_signup4.html',locals(),context_instance=RequestContext(request))
def start3(request):
    if  request.method ==   'POST':                
        string = request.POST.get('username', '')
        consumer_key="YSXHMWFQnu3GwhpIQzPxWQ"
        consumer_secret="JoENQsyTtXOkP1UJHznDjSWPFcdgADZToFgHupKCjc"
        access_token="1042496521-HfQSfLjfARBeE2TnvVL5W8ujrop9R3kAHC7GhI8"
        access_token_secret="ypK48se8H1VX1q3GMQ0jo0VU5qNmUEmkGJC50CUk6PE"

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
	
        api = tweepy.API(auth)



        trend = api.search( string, result_type = "popular" )

        i = 0
        final = [[]]
        jobj = {}

        for t in trend:
	        if i >= 2:
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
        place=[]
        name = []
        for k in places:
            place.append(k)       
        for n in names:
            name.append(n)
            

        response_dict = json.dumps( place )
        naam = json.dumps( name )
    return render_to_response('complete_signup6.html',locals(),context_instance=RequestContext(request))
def carousel(request):
    return render_to_response('try.html',locals(),context_instance=RequestContext(request))
def trya(request):
    return render_to_response('try.html',locals(),context_instance=RequestContext(request))
def screenname(request):
    if request.method == 'POST':
        print "screenname"                    
        string = request.POST.get('username', '')
        consumer_key="qWVpfFuvvwLVJ4WoNQF1A"
        consumer_secret="QWjguzmkawd7MVaXIWsG3OAYQLLdd7NdJOKXqdTpk"
        print string
        # The access tokens can be found on your applications's Details
        # page located at https://dev.twitter.com/apps (located 
        # under "Your access token")
        access_token="1271524633-TQasbVjkr5HFYeQiYYkMEaem6Vn08fis3wtGnBa"
        access_token_secret="WTz42fSDDtuLCDLmL8d0hkkubZxyekwEd7QWa6yFOq8"

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

        #hardcoding th query for now	
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

        # befor getting the first tweet not retweet
        # now getting the first five tweets	
        tweet = []      
        j = 0  
        for status in timeline:
            if status.text[0] != 'R' or status.text[1] != 'T':	
                tweet.append( status )
                j = j + 1
            if j >= 5:
                break

#        print tweet.text	
 
		

        final =  [[]]
        array = []
        arraynames = []
        i = 0 

        jobj = {}

        for tw in tweet:

            retweets = api.retweets(tw.id_str, 100)

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
        places=[]
        names = []
        for k in place:
            places.append(k)       
        for n in name:
            names.append(n)
            
        response_dict=json.dumps(places);
        naam=json.dumps(names);
        print "igotoutyipee"

    return render_to_response('complete_signup4.html',locals(),context_instance=RequestContext(request))
def hashtags(request):
    if request.method == 'POST':
        print "hashtag"                    
        string = request.POST.get('username', '')

        consumer_key="qWVpfFuvvwLVJ4WoNQF1A"
        consumer_secret="QWjguzmkawd7MVaXIWsG3OAYQLLdd7NdJOKXqdTpk"
        access_token="1271524633-TQasbVjkr5HFYeQiYYkMEaem6Vn08fis3wtGnBa"
        access_token_secret="WTz42fSDDtuLCDLmL8d0hkkubZxyekwEd7QWa6yFOq8"

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
	
        api = tweepy.API(auth)

       

        trend = api.search( string, result_type = "popular" )

        i = 0
        final = [[]]
        jobj = {}

        for t in trend:
	        if i >= 2:
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
        place=[]
        name = []
        for k in places:
            place.append(k)       
        for n in names:
            name.append(n)
            

        response_dict = json.dumps( place )
        naam = json.dumps( name )        
    return render_to_response('complete_signup4.html',locals(),context_instance=RequestContext(request))
def retweets(request):
    if request.method == 'POST':
        print "hashtag"                    
        
    return render_to_response('retweets.html',locals(),context_instance=RequestContext(request))
def start4(request):
# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
    if request.method == 'POST':
        string = request.POST.get('username', '')

        consumer_key="YSXHMWFQnu3GwhpIQzPxWQ"
        consumer_secret="JoENQsyTtXOkP1UJHznDjSWPFcdgADZToFgHupKCjc"
        access_token="1042496521-HfQSfLjfARBeE2TnvVL5W8ujrop9R3kAHC7GhI8"
        access_token_secret="ypK48se8H1VX1q3GMQ0jo0VU5qNmUEmkGJC50CUk6PE"

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

        #hardcoding th query for now	
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

        # befor getting the first tweet not retweet
        # now getting the first five tweets	
        followers = person.followers_count        
        tweet = []      
        j = 0  
        no_of_retweets = 0
        for status in timeline:
            if status.text[0] != 'R' or status.text[1] != 'T':	
                tweet.append( status )
                no_of_retweets = no_of_retweets + status.retweet_count
                j = j + 1
            if j >= 5:
                break

#        print tweet.text	
 
		

        final =  [[]]
        array = []
        arraynames = []
        i = 0 

        jobj = {}

        for tw in tweet:

            retweets = api.retweets(tw.id_str, 100)

            for trend in retweets:

            #	if i >= 50:
            #		break
                print trend.user.screen_name
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
        places=[]
        names = []
        for k in place:
            places.append(k)       
        for n in name:
            names.append(n)
            
        response_dict=json.dumps(places);
        naam=json.dumps(names);

        avgretweet = (float (no_of_retweets)) / 5

        ment = api.search( "@" + person.screen_name, result_type = "recent", rpp = 100 )

        k = 0
        for mention in ment:
        	k = k + 1

        ment_start_time = ment[0].created_at
        ment_end_time = ment[k-1].created_at
        dt=ment_start_time-ment_end_time
        minutes=dt.total_seconds()/60

        influence =( ( followers + ( avgretweet * 209 )  + ( ( k / minutes ) * 100000 ))/94553178)*100

        print "impact"
        impact=(float((avgretweet * 209)) / 94553178)*100
        print "reach"
        reach=(float(followers) / 94553178)*100
        print "buzz"
        buzz=(((float(float(k) / minutes) ) * 100000 ) / 94553178)*100
        
        
        
    return render_to_response('complete_signup5.html',locals(),context_instance=RequestContext(request))

