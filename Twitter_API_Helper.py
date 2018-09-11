####################################################################
##
##	Authors:		Peter Zorzonello
##	Last Update:	9/9/2018
##  Class:          EC601 - A1
##  File_Name:		Twitter_API_Helper.py
##
##	Description:	This is a library file containing functions that 
##                    utilize the Tweepy API.
##
####################################################################

#import required libraries
import tweepy
import twitter_globals_secret
import os

####################################################################
##
## Function Authenticate
##
## Description
##   This procedure uses the consumer key and secret, as well as 
##    the access token and secret to authenticate with Twitter.
##    Authentication uses OAuth
## 
## Inputs
##   None
##
## Outputs
##   An instance of the Tweepy API. 
##
## Exception Handling
##   Error messages are printed to the console
##   If the process could not authenticate with Twitter the process 
##     is terminated.
##
####################################################################
def authenticate():
	#this is the consumer key and secret, needed to authenticate with Twitter
	CONSUMER_KEY = twitter_globals_secret.CONSUMER_KEY
	CONSUMER_SECRET = twitter_globals_secret.CONSUMER_SECRET
	ACCESS_TOKEN = twitter_globals_secret.ACCESS_TOKEN
	ACCESS_TOKEN_SECRET = twitter_globals_secret.ACCESS_TOKEN_SECRET
	CONSUMER_SECRET2= twitter_globals_secret.CONSUMER_SECRET2

	print ("\n\nChecking on Twitter.com.......")

	#check on twitter.com by pinging it. If it repsonds we know 1) we have an internet connection and 2) Twitter.com is up
	if os.system("ping -c 1 twitter.com >nul 2>&1"):
		#if Twitter could not be reached then alert the user
		print("\n")
		print("Could not reach Twitter.")
		print("Please check your internet connection and try again.")
		print("If the problem percists then Twitter could be down.\n\n")
		exit(1)

	else:
		print("Twitter is live!")

		try:
			auth = tweepy.OAuthHandler(CONSUMER_KEY, ACCESS_TOKEN_SECRET)
			auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

			clientApi = tweepy.API(auth)
			return clientApi
		
		except tweepy.TweepError:
			print ("Unable to authenticate with Twitter.\n Program is terminating.\n\n")
			exit(1)

####################################################################
##
## Function FindUser
##
## Description
##   This attempts to find a Twitter profile. It prompts the user
##    to enter a Twitter handle, if the handle is valid, and 
##    if it can find the user it returns the Twitter handle.
##    If it cannot find the user or the handle is not in the correct 
##    format it will keep prompting the user until they exit. 
## 
## Inputs
##   api: An instance of the tweepy API, needed to call the API functions
##
## Outputs
##   A Twitter handle
##
## Exception Handling
##   Error messages are printed to the console
##   If the user cannot provide a valid Twitter handle the process
##    terminates.
##
####################################################################
#def findUser(api):

###################################################################
##
## Function getTweets
##
## Description
##   This procedure returns all the tweets from a user's timeline
## 
## Inputs
##   api: An instance of the tweepy API, needed to call the API functions
##   userName: A Twitter handle. The user's who's tweets to get.
##
## Outputs
##   An array of Tweet objects
##
## Exception Handling
##   Error messages are printed to the console
##
####################################################################
#def getTweets(api, userName):


###################################################################
##
## Function filterTweetsForImages
##
## Description
##   This procedure examines all the tweets provided and filters
##    out any non-image tweets. 
## 
## Inputs
##   api: An instance of the tweepy API, needed to call the API functions
##   tweets: An array of tweet objects
##
## Outputs
##   An array of Tweet objects that contain images
##
## Exception Handling
##   Error messages are printed to the console
##
####################################################################
#def filterTweetsForImages(api, tweets):

###################################################################
##
## Function filterTweetsForImages
##
## Description
##   This procedure goes through each tweet and downloads the image
## 
## Inputs
##   api: An instance of the tweepy API, needed to call the API functions
##   imageTweets: An array of tweet objects containing images
##
## Outputs
##   None
##
## Exception Handling
##   Error messages are printed to the console
##
####################################################################
#def downloadImages(api, imageTweets):