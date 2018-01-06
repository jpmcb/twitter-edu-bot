#!/usr/bin/python

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client.twitterEdu

schedule = db.class_schedule

data = {
	'class': '161',
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

insertion = schedule.insert_one(data)
print 'Class schedule entered: '.format(insertion.inserted_id)
