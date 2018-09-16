####################################################################
##
##  Authors:		Peter Zorzonello
##  Last Update:	9/15/2018
##  Class:			EC601 - A1
##  File_Name:		Main.py
##
##  Description:	
##    This is a control file used to test and call the library 
##      functions created as part of the first Mini-Project
##
####################################################################

#Import the required libraries
import Twitter_API_Helper
import FFMPEG_API_Helper
import Google_API_Helper


####################################################################
##
## Function Main
##
## Description
##   This is the main procedure of this test stub. It calls the 
##    library functions that access the different APIs.
## 
## Inputs
##   None
##
## Outputs
##   None
##
## Exception Handling
##   Error messages are printed to the console
##
####################################################################
def main():
	#TODO: Call the library functions 
	print("\n\nStarting API Project")

	#authenticate with Twitter
	twitterClient = Twitter_API_Helper.authenticate()
	
	#find a user
	user = Twitter_API_Helper.findUser(twitterClient)

	#get all their tweets
	tweets = Twitter_API_Helper.getTweets(twitterClient, user)

	#filter tweets for images and download the images to path
	path = Twitter_API_Helper.filterTweetsForImages(twitterClient, tweets, user)
	
	#reform all images in path to be the same size
	FFMPEG_API_Helper.reformatImages(path)

	#make the images into a video, if falue status will be 1
	status = FFMPEG_API_Helper.mergeImages(path)

	if status == 1:
		print ("FFMPEG could not make video. Terminating")
		exit(1)

	print("\nEnding API Project\n\n")




#Call the main function
main()
