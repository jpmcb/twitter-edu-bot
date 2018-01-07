#!/usr/bin/python
# tweetbot.py

import tweepy
from credentials import *

# OAuthHandler instance, required by Twitter for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# API instance
api = tweepy.API(auth)

# Send direct message to handle with msg
def dm_reminder(handle, msg):
    api.send_direct_message(handle, text=msg)

if __name__ == '__main__':
    # Ex. Can wrap function with due date detecting functions from mongo db module
    dm_reminder("@Bareous", "You have an assignment due!")
