import tweepy
import requests
from keys import *
import json
import locale
import datetime
today=datetime.date.today()
tomorrow = today + datetime.timedelta(days = 1) 
print(str(today)+'T03:07:43')



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)#Authenticating the keys
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

response=requests.get('https://clist.by/api/v1/contest/',params={'username':'hritikisfab1' ,'api_key':'d209f0890f40ddf422aa607f53fcade93d75804f','start__gt':str(today)+'T00:00:01','end__lt':str(tomorrow)+'T00:00:01'})
data=response.json()
contest_data=data["objects"]

def code_tweet():
    for i in contest_data:
        tweet= f"""
    Today's Coding Competition:
    Contest Name :{i['event']}
    String time : {i['start']}
    Ending time : {i['end']}
    Link to conest : {i['href']}
    #code #competitivecoding #codingislife    
        """
        try:
            api.verify_credentials()
            print('Authentication Successful')
        except:
            print('Error while authenticating API')
            sys.exit(1)
        try:
            api.update_status(tweet)
            print("Tweet Successful")
        except tweepy.TweepError as error:
            if error.api_code == 187:
                print("Duplicate message")  	#Duplicate tweets wil not be tweeted
            else:
                raise error

code_tweet()