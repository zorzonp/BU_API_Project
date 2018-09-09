####################################################################
##
##	Authors:		Peter Zorzonello
##	Last Update:	9/9/2018
##  Class:          EC601 - A1
##  File_Name:		Twitter_API_Helper.py
##
##	Description:	This is a library file contaning functions that 
##                    utlize the Tweepy API.
##
####################################################################

#import required liraries
import tweepy

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

####################################################################
##
## Function FindUser
##
## Description
##   This attempts to find a Twitter profile. It prompts the user
##    to enter a Twitter handle, if the handle is valid, and 
##    if it can find the user it returns the Twitter handle.
##    If it cannot find the user or the hndle is not in the correct 
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
def findUser(api):

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
def getTweets(api, userName):

###################################################################
##
## Function filterTweetsForImages
##
## Description
##   This procedure examins all the tweets provided and filters
##    out any non image tweets. 
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
def filterTweetsForImages(api, tweets):

###################################################################
##
## Function filterTweetsForImages
##
## Description
##   This procedure goes through each tweet and downloads the image
## 
## Inputs
##   api: An instance of the tweepy API, needed to call the API functions
##   imageTweets: An array of tweet objects contaning images
##
## Outputs
##   None
##
## Exception Handling
##   Error messages are printed to the console
##
####################################################################
def downloadImages(api, imageTweets):


