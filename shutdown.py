#!/usr/bin/python
import datetime
import os
from time import sleep
import subprocess

SYSTEM_HOUR_DEFAULT = 18
SYSTEM_MINUTE_RANGE_START = 7
SYSTEM_MINUTE_RANGE_END = 12
DEFAUTL_SLEEP_TIME = 5*60

def sendNotification(title, message):
	os.system("""
    osascript -e 'display notification "{}" with title "{}"'
    """.format(title, message))
	return

def isShutdownHour():
	return datetime.datetime.now().hour >= SYSTEM_HOUR_DEFAULT

def isInShutdownMinute():
	systemMinute = getSystemMinute();
	return systemMinute > SYSTEM_MINUTE_RANGE_START and systemMinute < SYSTEM_MINUTE_RANGE_END

def timeToShutDown():
	systemMinute = getSystemMinute();
	return systemMinute >= SYSTEM_MINUTE_RANGE_END

def getSystemMinute():
	return datetime.datetime.now().minute

if __name__ == '__main__':
	print "Starting the shutdown script";
	while True:
		print "Waking up"
		remainingTime = DEFAUTL_SLEEP_TIME;
		if isShutdownHour():
			if isInShutdownMinute():
				remainingTime = SYSTEM_MINUTE_RANGE_END - getSystemMinute();
				sendNotification("Shutdown Reminder", 
					"Shutdown in {} min. Save your work".format(remainingTime))
			elif timeToShutDown():
				sendNotification("Shutdown Reminder", 
					"Shutdown down. Happy Reading!!!")
				subprocess.call(['osascript', '-e', 'tell app "System Events" to shut down'])
		print "Sleeping for {} seconds".format(remainingTime)
		sleep(remainingTime);		
