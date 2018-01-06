#!/usr/bin/python

import time
import datetime
from pymongo import MongoClient

# Connect to Mongo
client = MongoClient('mongodb://localhost:27017')

# Establish the db
db = client.twitterEdu

# Establish the class_schedule collection
schedule = db.class_schedule

# CS 161 Schedule
data1 = {
	'class': 'CS 161',
	'schedule': {
		'Assignment 1': '01/14/2018',
		'Assignment 2': '01/21/2018',
		'Assignment 3': '01/28/2018',
		'Assignment 4': '02/04/2018',
		'Assignment 5': '02/18/2018',
		'Assignment 6': '02/25/2018',
		'Assignment 7': '03/04/2018',
		'Assignment 8': '03/11/2018',
		'Midterm': '02/11/2018',
		'Final': '03/18/2018'	
	}
}

# CS 162 Schedule
data2 = {
	'class': 'CS 162',
	'schedule': {
		'Assignment 1': '01/14/2018',
		'Assignment 2': '01/21/2018',
		'Assignment 3': '01/28/2018',
		'Assignment 4': '02/04/2018',
		'Assignment 5': '02/18/2018',
		'Assignment 6': '02/25/2018',
		'Assignment 7': '03/04/2018',
		'Assignment 8': '03/11/2018',
		'Midterm': '02/11/2018',
		'Final': '03/18/2018'	
	}
}

# CS 225 Schedule
data3 = {
	'class': 'CS 225',
	'schedule': {
		'Assignment 1': '01/14/2018',
		'Assignment 2': '01/21/2018',
		'Assignment 3': '01/28/2018',
		'Assignment 4': '02/04/2018',
		'Assignment 5': '02/18/2018',
		'Assignment 6': '02/25/2018',
		'Assignment 7': '03/04/2018',
		'Assignment 8': '03/11/2018',
		'Midterm': '02/11/2018',
		'Final': '03/18/2018'	
	}
}

# Insert the class schedules into the collection class_schedule
insertion = schedule.insert_one(data1)
print insertion
insertion = schedule.insert_one(data2)
print insertion
insertion = schedule.insert_one(data3)
print insertion

# Will check if an upcoming assignment is due soon (3 days)
def is_due(assignment_date):
	# Get the unix timestamp for the current time
	curr_date = time.time()
	
	# Get the unix timestamp for the due date
	due = time.mktime(datetime.datetime.strptime(assignment_date, "%m/%d/%Y").timetuple())
	
	# Get the difference between the current time and the due date,
	# and convert into the number of days
	num_days = (due - curr_date)/60/60/24
	
	# If the assignment is due soon, return 1
	if num_days <= 10.0 and num_days >= 0:
		return 1
	# Else return 0 for not being due soon
	else:
		return 0
	
# Grab the schedules for all the classes
class_schedules = db.class_schedule.find()

# Go through each class schedule, and determine if any assignments are due soon
for c in class_schedules:
	for assignment in c['schedule']:		
		if is_due(c['schedule'][assignment]):
			print assignment + " for " + c['class'] + " is due on " + c['schedule'][assignment]