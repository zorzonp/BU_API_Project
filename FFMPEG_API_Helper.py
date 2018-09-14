####################################################################
##
##	Authors:		Peter Zorzonello
##	Last Update:	9/14/2018
##  Class:          EC601 - A1
##  File_Name:		FFMPEG_API_Helper.py
##
##	Description:	This is a library file used to access the FFMPEG
##                   API
##
####################################################################

#import required libraries
import os
import ffmpy

####################################################################
##
## Function mergeImages
##
## Description
##   This function takes images stored in a common area and merges
##    them into a video format. The video is stored at the same 
##    location as the images.
## 
## Inputs
##   path: The path to the image directory, where the video lives
##
## Outputs
##   None
##
## Exception Handling
##   Error messages are printed to the console
##
####################################################################
def mergeImages(path):


	#if the video exists, remove it. If not then it could error out.
	os.system("rm "+path+"out_video.m4v")

	#runs the ffmpeg
	try:
		os.system("ffmpeg -pattern_type glob -framerate 0.1 -i '"+path+"*.jpg'  "+path+"out_video.m4v")
	except:
		print("Could not generate video from images. Process needs to exit.")
		exit(1)

