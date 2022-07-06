# Section 13.7-13.11 snippets with Self Checks
# because those sections are one running IPython session

# 13.7 Authenticating with Twitter Via Tweepy 
import tweepy

import keys

# Creating and Configuring an OAuthHandler to Authenticate with Twitter
auth = tweepy.OAuthHandler(keys.consumer_key,
                           keys.consumer_secret)

auth.set_access_token(keys.access_token,
                      keys.access_token_secret)

# Creating an API Object
api = tweepy.API(auth, wait_on_rate_limit=True, 
                 wait_on_rate_limit_notify=True)
                 
# 13.8 Getting Information About a Twitter Account
nasa = api.get_user('nasa')

# Getting Basic Account Information
nasa.id

nasa.name

nasa.screen_name

nasa.description

# Getting the Most Recent Status Update
nasa.status.text

# Getting the Number of Followers
nasa.followers_count

# Getting the Number of Friends 
nasa.friends_count

# Getting Your Own Account’s Information

# Self Check Exercise 3
nasa_kepler = api.get_user('NASAKepler')

nasa_kepler.followers_count

nasa_kepler.status.text

# 13.9 Introduction to Tweepy Cursors: Getting an Account’s Followers and Friends
# 13.9.1 Determining an Account’s Followers 
followers = []

# Creating a Cursor
cursor = tweepy.Cursor(api.followers, screen_name='nasa')

# Getting Results
for account in cursor.items(10):
    followers.append(account.screen_name)
    
print('Followers:', 
      ' '.join(sorted(followers, key=lambda s: s.lower())))
    
# Automatic Paging

# Getting Follower IDs Rather Than Followers

# Self Check Exercise 3
kepler_followers = []

cursor = tweepy.Cursor(api.followers, screen_name='NASAKepler')

for account in cursor.items(10):
    kepler_followers.append(account.screen_name)
    
print(' '.join(kepler_followers))

# 13.9.2 Determining Whom an Account Follows 
friends = []

cursor = tweepy.Cursor(api.friends, screen_name='nasa')

for friend in cursor.items(10):
    friends.append(friend.screen_name)

print('Friends:', 
      ' '.join(sorted(friends, key=lambda s: s.lower())))
    
# 13.9.3 Getting a User’s Recent Tweets
nasa_tweets = api.user_timeline(screen_name='nasa', count=3)

for tweet in nasa_tweets:
    print(f'{tweet.user.screen_name}: {tweet.text}\n')
    
# Grabbing Recent Tweets from Your Own Timeline

# Self Check 2
kepler_tweets = api.user_timeline(
    screen_name='NASAKepler', count=2)
    
for tweet in kepler_tweets:
    print(f'{tweet.user.screen_name}: {tweet.text}\n')

# 13.10 Searching Recent Tweets
# Tweet Printer
from tweetutilities import print_tweets

# Searching for Specific Words
tweets = api.search(q='Mars Opportunity Rover', count=3)

print_tweets(tweets)

# Searching with Twitter Search Operators
tweets = api.search(q='from:nasa since:2018-09-01', count=3)

print_tweets(tweets)

# Searching for a Hashtag
tweets = api.search(q='#collegefootball', count=20)

print_tweets(tweets)

# Self Check 3
tweets = api.search(q='astronaut from:nasa', count=1)

print_tweets(tweets)

# 13.11 Spotting Trends with the Twitter Trends API
# 13.11.1 Places with Trending Topics
trends_available = api.trends_available()

len(trends_available)

trends_available[0]

trends_available[1]

# 13.11.2 Getting a List of Trending Topics
# Worldwide Trending Topics
world_trends = api.trends_place(id=1)

trends_list = world_trends[0]['trends']

trends_list[0]

trends_list = [t for t in trends_list if t['tweet_volume']]

from operator import itemgetter 

trends_list.sort(key=itemgetter('tweet_volume'), reverse=True) 

for trend in trends_list[:5]:
    print(trend['name'])
    
# New York City Trending Topics
nyc_trends = api.trends_place(id=2459115)  # New York City WOEID

nyc_list = nyc_trends[0]['trends']

nyc_list = [t for t in nyc_list if t['tweet_volume']]

nyc_list.sort(key=itemgetter('tweet_volume'), reverse=True) 

for trend in nyc_list[:5]:
    print(trend['name'])
    
# Self Check 3
us_trends = api.trends_place(id='23424977')

us_list = us_trends[0]['trends']

us_list = [t for t in us_list if t['tweet_volume']]

us_list.sort(key=itemgetter('tweet_volume'), reverse=True)

for trend in us_list[:3]:
    print(trend['name'])
    
# 13.11.3 Create a Word Cloud from Trending Topics
topics = {}

for trend in nyc_list:
    topics[trend['name']] = trend['tweet_volume']
    
from wordcloud import WordCloud

wordcloud = WordCloud(width=1600, height=900,
    prefer_horizontal=0.5, min_font_size=10, colormap='prism', 
    background_color='white')                   

wordcloud = wordcloud.fit_words(topics)

wordcloud = wordcloud.to_file('TrendingTwitter.png')

# Self Check 1
topics = {}

for trend in us_list:
    topics[trend['name']] = trend['tweet_volume']

wordcloud = wordcloud.fit_words(topics)

wordcloud = wordcloud.to_file('USTrendingTwitter.png')




##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 13.12 snippets

import preprocessor as p 

p.set_options(p.OPT.URL, p.OPT.RESERVED)

tweet_text = 'RT A sample retweet with a URL https://nasa.gov'

p.clean(tweet_text)





##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
########################################################################## Section 13.13.2 snippets
# Authenticating
import tweepy

import keys

auth = tweepy.OAuthHandler(keys.consumer_key, 
                           keys.consumer_secret)               

auth.set_access_token(keys.access_token, 
                      keys.access_token_secret)
                 
api = tweepy.API(auth, wait_on_rate_limit=True, 
                 wait_on_rate_limit_notify=True)               

# Creating a TweetListener 
from tweetlistener import TweetListener

tweet_listener = TweetListener(api)

# Creating a Stream 
tweet_stream = tweepy.Stream(auth=api.auth, 
                             listener=tweet_listener)
                 
# Starting the TweetListeneret Stream
tweet_stream.filter(track=['Mars Rover'], is_async=True) 

# Asynchronous vs. Synchronous Streams

# Other filter Method Parameters

# Twitter Restrictions Note

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 13.15.1 snippets

# Get the API Object
from tweetutilities import get_API

api = get_API()

# Collections Required By LocationListener
tweets = [] 

counts = {'total_tweets': 0, 'locations': 0}

# Creating the LocationListener 
from locationlistener import LocationListener

location_listener = LocationListener(api, counts_dict=counts, 
    tweets_list=tweets, topic='football', limit=50)  

# Configure and Start the Stream of Tweets
import tweepy

stream = tweepy.Stream(auth=api.auth, listener=location_listener)

stream.filter(track=['football'], languages=['en'], is_async=False)

# Displaying the Location Statistics
counts['total_tweets']

counts['locations']

print(f'{counts["locations"] / counts["total_tweets"]:.1%}')

# Geocoding the Locations
from tweetutilities import get_geocodes

bad_locations = get_geocodes(tweets)

# Displaying the Bad Location Statistics
bad_locations

print(f'{bad_locations / counts["locations"]:.1%}')

# Cleaning the Data
import pandas as pd

df = pd.DataFrame(tweets)

df = df.dropna()

# Creating a Map with Folium
import folium

usmap = folium.Map(location=[39.8283, -98.5795], tiles='Stamen Terrain',
                   zoom_start=5, detect_retina=True)

# Creating Popup Markers for the Tweet Locations
for t in df.itertuples():
     text = ': '.join([t.screen_name, t.text])
     popup = folium.Popup(text, parse_html=True)
     marker = folium.Marker((t.latitude, t.longitude), 
                            popup=popup)
     marker.add_to(usmap)

# Saving the Map
usmap.save('tweet_map.html')




##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
# Section 15.2 Self Check snippets

# Exercise 1
import keys

from geopy import OpenMapQuest

geo = OpenMapQuest(api_key=keys.mapquest_key)

geo.geocode('Chicago, IL')


##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
