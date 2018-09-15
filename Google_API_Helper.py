####################################################################
##
##	Authors:		  Peter Zorzonello
##	Last Update:	9/10/2018
##  Class:        EC601 - A1
##  File_Name:		Google_API_Helper.py
##
##	Description:	This is a library file containing functions that 
##                    utilize the Google Vision API
##
####################################################################

####################################################################
##
## Function Authenticate
##
## Description
##   This procedure authenticates with the Google services using a 
##    locally stored JSON file.
## 
## Inputs
##   None
##
## Outputs
##   An instance of the Google API. 
##
## Exception Handling
##   Error messages are printed to the console
##   If the process could not authenticate with Google the process 
##     is terminated.
##
####################################################################
#def authenticate():

####################################################################
##
## Function openVideo
##
## Description
##   This procedure opens a video file stored locally
## 
## Inputs
##   api: Instance of the Google API, needed for API calls
##
## Outputs
##   An opened video file 
##
## Exception Handling
##   Error messages are printed to the console
##   If the file cannot be found or the file cannot be opened then 
##     the process will terminate. 
##
####################################################################
#def openVideo(api):

####################################################################
##
## Function annotate
##
## Description
##   This sends a video to Google to be annotated by their API
## 
## Inputs
##   api: Instance of the Google API, needed for API calls
##   video: The video to annotate
##
## Outputs
##   The annotated results returned by the API
##
## Exception Handling
##   Error messages are printed to the console
##   If the annotation was unsuccessful the process will terminate
##
####################################################################
#def annotate(api, video):

####################################################################
##
## Function annotate
##
## Description
##   This procedure loops over the results of an annotated video
##     and prints them to the console for the user
## 
## Inputs
##   api: Instance of the Google API, needed for API calls
##   results: the annotated results
##
## Outputs
##   None
##
## Exception Handling
##   Error messages are printed to the console
##
####################################################################
#def printResults(api, results):
