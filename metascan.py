#!/usr/bin/env python3


#=====================================================
#
# Metascan
#
#=====================================================
#
#
#@version	2.0
#@link		https://github.com/yourusername/metascan
#@authors	Chris Morris & Collin Mockbee

import os, sys
import errno
import subprocess
import string
import random
import shutil
import colorama
from colorama import Fore, Back, Style
from definitions import ROOT_DIR
from fileinteractions import stageset, checkdelete, jsonsort
from exiftool import exifJSON, exifHTML, exifHTMLDump
from filter import filterexec
from markups import filtershtml, rawmetahtml, hexmetahtml, statshtml 
from shutil import copyfile

def credits():
	"""
	Display application banner and welcome information.
	Prompts user to ensure files are placed in the media directory.
	"""
	print("")
	print("")
	print("███╗   ███╗███████╗████████╗ █████╗ ███████╗ ██████╗ ███████╗ █████╗ ███╗   ██╗")
	print("████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔════╝ ██╔════╝██╔══██╗████╗  ██║")
	print("██╔████╔██║█████╗     ██║   ███████║█████╗  ██║      ███████╗███████║██╔██╗ ██║")
	print("██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██╔══╝  ██║      ╚════██║██╔══██║██║╚██╗██║")
	print("██║ ╚═╝ ██║███████╗   ██║   ██║  ██║██║     ╚██████╗ ███████║██║  ██║██║ ╚████║")
	print("╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝")
	print("")
	print("")
	print(Fore.WHITE + "An OSINT Metadata analyzing tool that filters through tags and creates reports")
	print("Version 2.0")
	print(Style.RESET_ALL)
	print(Fore.GREEN + "Authors: Chris Morris & Collin Mockbee")
	print("github.com/yourusername/metascan")
	print()
	print("=========================================================")
	print(Style.RESET_ALL)
	print(Fore.RED + "Remember to place the files you wish to analyze in this directory!")
	print(Style.BRIGHT +"-->  "+ ROOT_DIR + "/media  <--")
	print(Style.RESET_ALL)
	input("Press [ENTER] to continue")
	print()
	
def condchecking():
	"""
	Verify system conditions and prepare directories for analysis.
	Checks and sets up required directory structure, prompts for cleanup if needed.
	"""
	print("=======================Step 1: Condition Checking =======================")
	print()
	print("Need to check to make sure that the program will run correctly...")
	print()
	input("Press [ENTER] to continue")

	try:
		stageset()
		checkdelete()
		print()
		print(Fore.GREEN + "Done. Everything looks correct")
		print(Style.RESET_ALL)

	except IOError as er:
		errno,strerror = er.args
		print(Fore.RED + "I/O error({0}): {1}".format(errno,strerror))
		print(Style.RESET_ALL)


	except:
		 print(Fore.RED + "Error:", sys.exc_info()[0])
		 print(Style.RESET_ALL)

def projectcreation():
	"""
	Create a new project directory for analysis results.
	User can provide a custom name or use an auto-generated one.
	Returns the path to the created project directory.
	"""
	print("=========================Step 2: Project Creation=========================")

	randominput = ''.join(random.choice(string.ascii_lowercase 
		+ string.digits) for _ in range(6))

	print()
	print()
	print("Enter a name for your project. It will also be the name of the directory.")
	print("(If you would like a random name, leave it blank and press enter)")
	print()
	userproj = input("Project Name--> ") 
	print()

	if not userproj:
		userproj = "proj_" + randominput
	try:
		os.makedirs(ROOT_DIR +"/User_Projects/"+ userproj, exist_ok=True)
		projectdir = ROOT_DIR + "/User_Projects/" + userproj 
		print(Style.BRIGHT + "Your project is named: " + userproj)
		print(Style.RESET_ALL)
		print(Fore.GREEN + "Successfully created project folder!")
		print(Style.RESET_ALL)

	except:
		print(Fore.RED + "ERROR: ", sys.exc_info()[0])
		sys.exit("Quitting. You need a project folder")
		print(Style.RESET_ALL)

	return projectdir

def exifrun():
	"""
	Execute ExifTool to extract metadata from files in the media directory.
	Generates JSON, HTML, and hexadecimal dump outputs for comprehensive analysis.
	"""
	print("=======================Step 3: Running the Exiftool=======================")
	print()

	print("This is going to run the exiftool on all of the media you defined here:")
	print(Fore.BLUE + ROOT_DIR + "/media")
	print(Style.RESET_ALL)
	print("It could take a while depending how many files you placed.")
	print()
	input("Press [ENTER] to continue")
	try:
		print()
		exifJSON()
	except:
		print(Fore.RED + "Exiftool to JSON failed")
		print("ERROR:", sys.exc_info()[0])
		print(Style.RESET_ALL)
		pass

	try:
		exifHTML()
	except:
		print(Fore.RED +"Exiftool to HTML failed")
		print("ERROR:", sys.exc_info()[0])
		print(Style.RESET_ALL)
		pass

	try:
		exifHTMLDump()
	except:
		print(Fore.RED +"Exiftool to Hexadecimal HTML failed")
		print("ERROR:", sys.exc_info()[0])
		print(Style.RESET_ALL)
		pass
	print()


def filtering():
	"""
	Sort and filter extracted metadata.
	Organizes JSON files by file type and applies intelligent filtering
	to extract only the most relevant metadata tags.
	"""
	print("=============================Step 4: Filtering=============================")
	print()

	jsondir = ROOT_DIR + "/exifdata/json/"
	jsonsubdirs = ['odp', 'png', 'mp3', 'dll', 'torrent', 'pptx', 'ods', 'odt,' 'zip', 'exe',
	 'xlsx', 'svg', 'pdf', 'mp4', 'html', 'docx', 'gif', 'wav', 'jpeg', 'mkv']

	print("Now going to sort the JSON into their respective (original) filetype folder")
	print()
	input("Press [ENTER] to continue")
	print()
	try:
		jsonsort()
		print(Fore.GREEN + "Sorting Successful in exifdata/json/")
		print(Style.RESET_ALL)

	except IOError as sorter:
		errno,strerror = sorter.args
		print(Fore.RED + "I/O error({0}): {1}".format(errno,strerror))
		print(Style.RESET_ALL)

	except:
		print(Fore.RED + "ERROR:", sys.exc_info()[0])
		print(Style.RESET_ALL)

	print("Starting Filtering Process...")

	try:
		filterexec()
		print(Fore.GREEN + "Filtering Successful!")
		print(Style.RESET_ALL)

	except IOError as filterer:
		errno,strerror = filterer.args
		print(Fore.RED + "I/O error({0}): {1}".format(errno,strerror))
		print(Style.RESET_ALL)


	except:
		print(Fore.RED +"ERROR:", sys.exc_info()[0])
		print(Style.RESET_ALL)


def makereport(PROJ_DIR):
	"""
	Generate comprehensive HTML reports and organize project directory.
	
	Creates multiple report views:
	- Statistics dashboard
	- Filtered metadata view
	- Raw metadata view
	- Hexadecimal dump view
	
	Args:
		PROJ_DIR: Path to the project directory where reports will be saved
	"""
	print("=========================Step 5: Make Report=========================")
	print()
	print("This will make the HTML reports and set up the User Project directory")
	print()
	input("Press [ENTER] to continue")
	print()

	def copyfolders(src, dest):
		"""
		Copy directory tree from source to destination.
		Handles both directories and individual files.
		"""
		try:
			shutil.copytree(src,dest)
		except OSERROR as exc:
			if exc.errno == errno.ENOTDIR:
				shutil.copy(src,dest)
			else:
				raise

	#Make HTML Reports			
	try:
		statshtml()
	except:
		print(Fore.RED + "ERROR: could not run stat html report", sys.exc_info()[0])
		print(Style.RESET_ALL)
	try:
		filtershtml()
	except:
		print(Fore.RED + "ERROR: could not run filter html report", sys.exc_info()[0])
		print(Style.RESET_ALL)
	try:
		rawmetahtml()	
	except:
		print(Fore.RED + "ERROR: could not run rawmetahtml report", sys.exc_info()[0])
		print(Style.RESET_ALL)
	try:
		hexmetahtml()
	except:
		print(Fore.RED + "ERROR: could not run hexmetahtml report", sys.exc_info()[0])
		print(Style.RESET_ALL)



	#Moving folders to project dir
	try:
		print("Copying exifdata to project directory")
		copyfolders(ROOT_DIR + "/exifdata/" , PROJ_DIR + "/exifdata/")
	except:
		print(Fore.RED + "ERROR: could not copy exifdata to project dir: ", sys.exc_info()[0])
		print(Style.RESET_ALL)
	try:
		print("Placing Template_Data into project dir...")
		copyfolders(ROOT_DIR + "/Template_Data/", PROJ_DIR + "/Template_Data/")
	except:
		print(Fore.RED + "ERROR: Failed to copy Template_Data: ",sys.exc_info()[0])
		print(Style.RESET_ALL)


	#Placing reports from ROOT_DIR to PROJ_DIR
	print("Placing reports into project dir...")
	try:
		copyfile(ROOT_DIR + "/" + "index.html", PROJ_DIR + "/index.html")
		os.remove(ROOT_DIR + "/" + "index.html")

	except:
		print(Fore.RED + "ERROR: Failed to copy index.html-- ",sys.exc_info()[0])
		print(Style.RESET_ALL)
			
	try:
		copyfile(ROOT_DIR + "/" + "filters.html", PROJ_DIR + "/filters.html")
		os.remove(ROOT_DIR + "/" + "filters.html")
		
	except:
		print(Fore.RED + "ERROR: Failed to copy filters.html-- ",sys.exc_info()[0])
		print(Style.RESET_ALL)
	
	try:
		copyfile(ROOT_DIR + "/" + "rawmeta.html", PROJ_DIR + "/rawmeta.html")
		os.remove(ROOT_DIR + "/" + "rawmeta.html")

	except:
		print(Fore.RED + "ERROR: Failed to copy rawmeta.html-- ",sys.exc_info()[0])
		print(Style.RESET_ALL)

	try:
		copyfile(ROOT_DIR + "/" + "hexdump.html", PROJ_DIR + "/hexdump.html")
		os.remove(ROOT_DIR + "/" + "hexdump.html")
	except:
		print(Fore.RED + "ERROR: Failed to copy rawmeta.html-- ",sys.exc_info()[0])
		print(Style.RESET_ALL)



	#Removing exifdata/ since it exsists in PROJ_DIR 	
	try:
		shutil.rmtree(ROOT_DIR + "/exifdata/")
	except:
		print(Fore.RED + "ERROR: Failed to remove /exifdata/ dir: ",sys.exc_info()[0])
		print(Style.RESET_ALL)


	#Setting up exifdata dir for next run
	try:
		print("Setting up exifdata directory...")
		stageset()

	except:
		print(Fore.RED + "Could not run the stageset function-- ", sys.exc_info()[0])
		print(Style.RESET_ALL)

	print()
	print(Fore.GREEN + "FINISHED!")
	print(Style.RESET_ALL)
	print(Style.BRIGHT + "Project Folder is here:")
	print(Style.RESET_ALL)
	print(Back.WHITE+ Fore.BLACK+ PROJ_DIR)
	print(Style.RESET_ALL)
	print(Style.BRIGHT+ "To view the Report, click on the index.html file")
	print(Style.RESET_ALL)
	print("===============================================================")
	print()
	sys.exit(0)

def main():
	"""
	Main application entry point.
	Executes the complete metadata analysis workflow.
	"""
	credits()
	condchecking()
	PROJ_DIR = projectcreation()
	exifrun()
	filtering()
	makereport(PROJ_DIR)


if __name__ == '__main__':
	main()
	
