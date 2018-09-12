####################################################################
##
##	Authors:		Peter Zorzonello
##	Last Update:	9/12/2018
##  Class:          EC601 - A1
##  File_Name:		Main.py
##
##	Description:	This is a control file used to test and call 
##                  the library functions created as part of 
##                  the first Mini-Project
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

    twitterClient = Twitter_API_Helper.authenticate()
    user = Twitter_API_Helper.findUser(twitterClient)
    tweets = Twitter_API_Helper.getTweets(twitterClient, user)
    Twitter_API_Helper.filterTweetsForImages(twitterClient, tweets, user)

    print("\nEnding API Project\n\n")




#Call the main function
main()