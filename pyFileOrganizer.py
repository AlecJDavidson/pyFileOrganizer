# Name of the code: pyFileOrganizer
# Author of the code: Alec J. Davidson
# Version of the code and the date of its last revision: 08/30/19 Ver. 1.7

# This is a script that will automatically move files from /Downloads
# to the respective directory based on the files extension.

# Variables used with a short description of the variable, 
# as well as the format of the data (e.g. datatype):

import os # Imports OS for file system access.
import shutil # Imports shutil to safely move files.
import filetype # Infers filetype and MIME type by checking the magic numbers signature of a file or butter.
import getpass # Allows username to be retrieved.

user = getpass.getuser() # Automatically retrieves username.

picType = ['jpg','png','gif','webp','ico']# Creates list of image file types.
musType = ['mp3','flac','wav']# Creates list of audio file types.
vidType = ['mkv','mp4','mov','wmv','mpg','flv','webm','m4v']# Creates list of video file types.
#proType = ['.deb'] # Creates a list of program file types.

mus_dir = '/home/'+user+'/Music/' # Music directory.
pic_dir = '/home/'+user+'/Pictures/' # Pictures directory.
vid_dir = '/home/'+user+'/Videos/' # Videos directory.
dow_dir = '/home/'+user+'/Downloads/' # Downloads directory

def move_vid(): # Changes destination variable to vid_dir and moves video files.
	destination = vid_dir
	shutil.move(files,destination)
def move_pic(): # Changes destination variable to pic_dir and moves video files.
	destination = pic_dir
	shutil.move(files,destination)
def move_mus(): # Changes destination variable to mus_dir and moves audio files.
	destination = mus_dir
	shutil.move(files,destination)

os.chdir(dow_dir) # Changes working directory to Downloads directory.
source = os.listdir(dow_dir) # Defines source.
for files in source:
	try:
		kind = filetype.guess(files)
		if kind.extension in vidType:
			move_vid()
		if kind.extension in picType:
			move_pic()
		if kind.extension in musType:
			move_mus()
	except PermissionError:
		print(PermissionError)
	except:
		print('There was an error moving all or some of your files.')
		print('There may be a file with an unknown file extension.')