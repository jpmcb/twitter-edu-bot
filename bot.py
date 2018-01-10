#!/usr/bin/python

import time
import datetime
import tweepy
from pymongo import MongoClient
from credentials import * 

consumer_key = 'XkoHqlQQI9vNNfOu8qHEl7k9R'
consumer_secret = 'tFCcPGrhr4Bni4zM43rN0JbbyOMxFh22Y24bQyS6cDAP5Pq2aK'
access_token = '949798552489705472-IPApLZMdATiNJDhPWVgvduXW6vb3cXH'
access_secret = 'GvDE9HLFTVZNG7pGp1qUw2cqYPwbfoiZQfdnYM33zxWnK'

# OAuthHandler instance, required by Twitter for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# Twitter API instance
api = tweepy.API(auth)

# Connect to Mongo
client = MongoClient('mongodb://heroku_wwpzkm46:96ichdg7jpbqvn7rj90nuaccvf@ds245277.mlab.com:45277/')

# Establish the db
db = client.heroku_wwpzkm46

# Establish the class_schedule collection
schedule = db.class_schedule

# The schedule for all classes
data = [
    {
        'class': '161',
        'schedule': {'Assignment 1': '01/14/2018', 'Assignment 2': '01/21/2018', 'Assignment 3': '01/28/2018',
                     'Assignment 4': '02/04/2018', 'Assignment 5': '02/18/2018', 'Assignment 6': '02/25/2018',
                     'Assignment 7': '03/04/2018', 'Assignment 8': '03/11/2018', 'Midterm': '02/11/2018',
                     'Final': '03/18/2018'}
    },
    {
        'class': '162',
        'schedule': {'Assignment 1': '01/14/2018', 'Assignment 2': '01/21/2018', 'Assignment 3': '01/28/2018',
                     'Assignment 4': '02/04/2018', 'Assignment 5': '02/18/2018', 'Assignment 6': '02/25/2018',
                     'Assignment 7': '03/04/2018', 'Assignment 8': '03/11/2018', 'Midterm': '02/11/2018',
                     'Final': '03/18/2018'}
    },
    {
        'class': '165',
        'schedule': {'Assignment 1': '01/14/2018', 'Assignment 2': '01/21/2018', 'Assignment 3': '01/28/2018',
                     'Assignment 4': '02/04/2018', 'Assignment 5': '02/18/2018', 'Assignment 6': '02/25/2018',
                     'Assignment 7': '03/04/2018', 'Assignment 8': '03/11/2018', 'Midterm': '02/11/2018',
                     'Final': '03/18/2018'}
    },
    {
        'class': '225',
        'schedule': {'Assignment 1': '01/14/2018', 'Assignment 2': '01/21/2018', 'Assignment 3': '01/28/2018',
                     'Assignment 4': '02/04/2018', 'Assignment 5': '02/18/2018', 'Assignment 6': '02/25/2018',
                     'Assignment 7': '03/04/2018', 'Assignment 8': '03/11/2018', 'Midterm': '02/11/2018',
                     'Final': '03/18/2018'}
    },
    {
        'class': '261',
        'schedule': {'Assignment 1': '01/14/2018', 'Assignment 2': '01/21/2018', 'Assignment 3': '01/28/2018',
                     'Assignment 4': '02/04/2018', 'Assignment 5': '02/18/2018', 'Assignment 6': '02/25/2018',
                     'Assignment 7': '03/04/2018', 'Assignment 8': '03/11/2018', 'Midterm': '02/11/2018',
                     'Final': '03/18/2018'}
    },
    {
        'class': '271',
        'schedule': {'Assignment 1': '01/14/2018', 'Assignment 2': '01/21/2018', 'Assignment 3': '01/28/2018',
                     'Assignment 4': '02/04/2018', 'Assignment 5': '02/18/2018', 'Assignment 6': '02/25/2018',
                     'Assignment 7': '03/04/2018', 'Assignment 8': '03/11/2018', 'Midterm': '02/11/2018',
                     'Final': '03/18/2018'}
    },
    {
        'class': '290',
        'schedule': {'Assignment 1': '01/14/2018', 'Assignment 2': '01/21/2018', 'Assignment 3': '01/28/2018',
                     'Assignment 4': '02/04/2018', 'Assignment 5': '02/18/2018', 'Assignment 6': '02/25/2018',
                     'Assignment 7': '03/04/2018', 'Assignment 8': '03/11/2018', 'Midterm': '02/11/2018',
                     'Final': '03/18/2018'}
    },
    {
        'class': '325',
        'schedule': {'Assignment 1': '01/14/2018', 'Assignment 2': '01/21/2018', 'Assignment 3': '01/28/2018',
                     'Assignment 4': '02/04/2018', 'Assignment 5': '02/18/2018', 'Assignment 6': '02/25/2018',
                     'Assignment 7': '03/04/2018', 'Assignment 8': '03/11/2018', 'Midterm': '02/11/2018',
                     'Final': '03/18/2018'}
    },
    {
        'class': '340',
        'schedule': {'Assignment 1': '01/14/2018', 'Assignment 2': '01/21/2018', 'Assignment 3': '01/28/2018',
                     'Assignment 4': '02/04/2018', 'Assignment 5': '02/18/2018', 'Assignment 6': '02/25/2018',
                     'Assignment 7': '03/04/2018', 'Assignment 8': '03/11/2018', 'Midterm': '02/11/2018',
                     'Final': '03/18/2018'}
    },
    {
        'class': '344',
        'schedule': {'Assignment 1': '01/14/2018', 'Assignment 2': '01/21/2018', 'Assignment 3': '01/28/2018',
                     'Assignment 4': '02/04/2018', 'Assignment 5': '02/18/2018', 'Assignment 6': '02/25/2018',
                     'Assignment 7': '03/04/2018', 'Assignment 8': '03/11/2018', 'Midterm': '02/11/2018',
                     'Final': '03/18/2018'}
    },
    {
        'class': '352',
        'schedule': {'Assignment 1': '01/14/2018', 'Assignment 2': '01/21/2018', 'Assignment 3': '01/28/2018',
                     'Assignment 4': '02/04/2018', 'Assignment 5': '02/18/2018', 'Assignment 6': '02/25/2018',
                     'Assignment 7': '03/04/2018', 'Assignment 8': '03/11/2018', 'Midterm': '02/11/2018',
                     'Final': '03/18/2018'}
    },
    {
        'class': '361',
        'schedule': {'Assignment 1': '01/14/2018', 'Assignment 2': '01/21/2018', 'Assignment 3': '01/28/2018',
                     'Assignment 4': '02/04/2018', 'Assignment 5': '02/18/2018', 'Assignment 6': '02/25/2018',
                     'Assignment 7': '03/04/2018', 'Assignment 8': '03/11/2018', 'Midterm': '02/11/2018',
                     'Final': '03/18/2018'}
    },
    {
        'class': '362',
        'schedule': {'Assignment 1': '01/14/2018', 'Assignment 2': '01/21/2018', 'Assignment 3': '01/28/2018',
                     'Assignment 4': '02/04/2018', 'Assignment 5': '02/18/2018', 'Assignment 6': '02/25/2018',
                     'Assignment 7': '03/04/2018', 'Assignment 8': '03/11/2018', 'Midterm': '02/11/2018',
                     'Final': '03/18/2018'}
    },
    {
        'class': '372',
        'schedule': {'Assignment 1': '01/14/2018', 'Assignment 2': '01/21/2018', 'Assignment 3': '01/28/2018',
                     'Assignment 4': '02/04/2018', 'Assignment 5': '02/18/2018', 'Assignment 6': '02/25/2018',
                     'Assignment 7': '03/04/2018', 'Assignment 8': '03/11/2018', 'Midterm': '02/11/2018',
                     'Final': '03/18/2018'}
    },
    {
        'class': '373',
        'schedule': {'Assignment 1': '01/14/2018', 'Assignment 2': '01/21/2018', 'Assignment 3': '01/28/2018',
                     'Assignment 4': '02/04/2018', 'Assignment 5': '02/18/2018', 'Assignment 6': '02/25/2018',
                     'Assignment 7': '03/04/2018', 'Assignment 8': '03/11/2018', 'Midterm': '02/11/2018',
                     'Final': '03/18/2018'}
    },
    {
        'class': '464',
        'schedule': {'Assignment 1': '01/14/2018', 'Assignment 2': '01/21/2018', 'Assignment 3': '01/28/2018',
                     'Assignment 4': '02/04/2018', 'Assignment 5': '02/18/2018', 'Assignment 6': '02/25/2018',
                     'Assignment 7': '03/04/2018', 'Assignment 8': '03/11/2018', 'Midterm': '02/11/2018',
                     'Final': '03/18/2018'}
    },
    {
        'class': '467',
        'schedule': {'Assignment 1': '01/14/2018', 'Assignment 2': '01/21/2018', 'Assignment 3': '01/28/2018',
                     'Assignment 4': '02/04/2018', 'Assignment 5': '02/18/2018', 'Assignment 6': '02/25/2018',
                     'Assignment 7': '03/04/2018', 'Assignment 8': '03/11/2018', 'Midterm': '02/11/2018',
                     'Final': '03/18/2018'}
    },
    {
        'class': '475',
        'schedule': {'Assignment 1': '01/14/2018', 'Assignment 2': '01/21/2018', 'Assignment 3': '01/28/2018',
                     'Assignment 4': '02/04/2018', 'Assignment 5': '02/18/2018', 'Assignment 6': '02/25/2018',
                     'Assignment 7': '03/04/2018', 'Assignment 8': '03/11/2018', 'Midterm': '02/11/2018',
                     'Final': '03/18/2018'}
    },
    {
        'class': '496',
        'schedule': {'Assignment 1': '01/14/2018', 'Assignment 2': '01/21/2018', 'Assignment 3': '01/28/2018',
                     'Assignment 4': '02/04/2018', 'Assignment 5': '02/18/2018', 'Assignment 6': '02/25/2018',
                     'Assignment 7': '03/04/2018', 'Assignment 8': '03/11/2018', 'Midterm': '02/11/2018',
                     'Final': '03/18/2018'}
    }
]

# Insert the class schedules into the collection class_schedule
for course in data:
    if db.class_schedule.find_one({'class': course['class']}) == None:
        db.class_schedule.insert_one(course)


# Will check if an upcoming assignment is due soon (3 days)
def is_due(assignment_date):
    # Get the unix timestamp for the current time
    curr_date = time.time()

    # Get the unix timestamp for the due date
    due = time.mktime(datetime.datetime.strptime(assignment_date, "%m/%d/%Y").timetuple())

    # Get the difference between the current time and the due date,
    # and convert into the number of days
    num_days = (due - curr_date) / 60 / 60 / 24

    # If the assignment is due soon, return 1
    if num_days <= 10.0 and num_days >= 0:
        return 1
    # Else return 0 for not being due soon
    else:
        return 0


# Will grab the twitter handles of students with a due date for a class
def grab_handles(course):
    return db.twitter_handles.find({"enrolled": course})


# Send direct message to handle with message
def dm_reminder(handle, message):
    api.send_direct_message(handle, text=message)


# Grab the schedules for all the classes
class_schedules = db.class_schedule.find()

# Go through each class schedule, and determine if any assignments are due soon
for course in class_schedules:
    # Get the student handles enrolled in course
    enrolled_students = grab_handles(course['class'])

    for assignment in course['schedule']:
        if is_due(course['schedule'][assignment]):
            for s in enrolled_students:
                handle = s['handle']
                # Indicates if assignment is due soon
                dueMsg = assignment + " for " + course['class'] + " is due on " + course['schedule'][assignment]

                dm_reminder(handle, dueMsg)
