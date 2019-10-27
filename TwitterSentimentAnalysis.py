# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 13:19:42 2019

@author: Mike Hickey

"""
"""
Data Science Libs

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels as sm

""" 
Sentiment Analysis - Add these Libraries
"""
from wordcloud import WordCloud, STOPWORDS
import TextBlob as tb
import tweepy as twp
from tweepy import OAuthHandler
"""

Twitter App Info

Consumer API keys
rXobhjL89PHmsttD99TGob403 (API key)
aFyurRJMqLBWmChwKbu7tKZE8HEDnSW6hSW1Q2Stw55BCaa7Cc (API secret key)

Access token & access token secret: 
17433271-1FRK73QG0LZvXH0QFUQfPRoJL9uEDW3z9DLWPDVm1 (Access token)
D4eBQk1BteQj1ZdO7yYvwbt9jRluGw67fx7ieyyojpdCV (Access token secret)

"""

consumer_key = 'rXobhjL89PHmsttD99TGob403'
consumer_secret = 'aFyurRJMqLBWmChwKbu7tKZE8HEDnSW6hSW1Q2Stw55BCaa7Cc'
access_token = '17433271-1FRK73QG0LZvXH0QFUQfPRoJL9uEDW3z9DLWPDVm1'
access_secret = 'D4eBQk1BteQj1ZdO7yYvwbt9jRluGw67fx7ieyyojpdCV'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = twp.API(auth)

for status in twp.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)