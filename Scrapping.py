#!/usr/bin/env python
# coding: utf-8

# In[79]:


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a twitter scraping program.
"""
import GetOldTweets3 as got
import pandas as pd
import numpy as np



text_query = ['Lockdown'] #
count = 100
maharashtra=["Pune", "Mumbai", "Delhi"]

# Function that pulls tweets based on a general search query and turns to csv file

# Parameters: (text query you want to search), (max number of most recent tweets to pull from)

def text_query_to_csv(text_query, count, place):
    # Creation of query object
    # Creation of query object
    leng = 0
    i=0
    while leng < count:
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(text_query[i]).setLang('en').setMaxTweets(count-leng).setNear(place).setSince("2020-05-28").setUntil("2020-05-31")

            # Creation of list that contains all tweets
        tweets = got.manager.TweetManager.getTweets(tweetCriteria)
            # Creating list of chosen tweet data
        text_tweets = [[place, text_query[0], tweet.date, tweet.text,tweet.id,tweet.username,tweet.geo,tweet.retweets,tweet.favorites,tweet.hashtags] for tweet in tweets]

            # Creation of dataframe from tweets
        if i == 0:
            tweets_df = pd.DataFrame(text_tweets, columns = ['Place', 'Query', 'Datetime', 'Text','TweetID','username','geo','retweets','favourites','hashtags'])
        else:
            temp = pd.DataFrame(text_tweets, columns = ['Place', 'Query', 'Datetime', 'Text','TweetID','username','geo','retweets','favourites','hashtags'])
            tweets_df = tweets_df.append(temp)
        leng = len(tweets_df)        
        
        if text_query[-1] == text_query[i]:
            break
        i+=1
        
    return tweets_df   
 
#     tweetCriteria = got.manager.TweetCriteria().setQuerySearch(text_query[0]).setLang('en').setMaxTweets(count).setNear(place).setSince("2020-05-28").setUntil("2020-05-31")
    
#     # Creation of list that contains all tweets
#     tweets = got.manager.TweetManager.getTweets(tweetCriteria)
#     # Creating list of chosen tweet data
#     text_tweets = [[place, text_query[0], tweet.date, tweet.text,tweet.id,tweet.username,tweet.geo,tweet.retweets,tweet.favorites,tweet.hashtags] for tweet in tweets]
#     print(f'len(text_tweets): {len(text_tweets)}')
#     tweets_df1 = pd.DataFrame(text_tweets, columns = ['Place', 'Query', 'Datetime', 'Text','TweetID','username','geo','retweets','favourites','hashtags'])
#     if len(text_tweets) < count:
#         print('True')
#         tweetCriteria = got.manager.TweetCriteria().setQuerySearch(text_query[1]).setLang('en').setMaxTweets(count-len(tweets_df1)).setNear(place).setSince("2020-05-28").setUntil("2020-05-31")
#         # Creation of list that contains all tweets
#         tweets = got.manager.TweetManager.getTweets(tweetCriteria)
#         # Creating list of chosen tweet data
#         temp2 = [[place, text_query[1], tweet.date, tweet.text,tweet.id,tweet.username,tweet.geo,tweet.retweets,tweet.favorites,tweet.hashtags] for tweet in tweets]
#         print(f'len(temp): {len(temp2)}')
#         tweets_df2 = pd.DataFrame(temp2, columns = ['Place', 'Query', 'Datetime', 'Text','TweetID','username','geo','retweets','favourites','hashtags'])
#         tweets_df1 = tweets_df1.append(tweets_df2)
    
#     # Creation of dataframe from tweets
    
    
#     return tweets_df1
    
df=pd.DataFrame()
temp=pd.DataFrame()
i=0
for place in maharashtra: 
    temp=text_query_to_csv(text_query, count, place)
    if i==0:
        df = temp
    else:
        df = df.append(temp)
    i+=1
    
df.to_csv('maharashtra.csv')
