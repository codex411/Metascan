#!/usr/bin/env python3

import pyexifinfo as exif
import os, sys
import subprocess
import json
from os.path import basename
from definitions import ROOT_DIR
import shutil
from progress.bar import Bar

"""
ExifTool integration module for metadata extraction.
Processes files and outputs metadata in JSON, HTML, and hexadecimal formats.
Requires ExifTool to be installed on the system.
"""


def exifJSON():
	"""
	Extract metadata from files in the media directory and output as JSON.
	Progress bar indicates processing status.
	"""
	print("Running exiftool to JSON")
	os.chdir(ROOT_DIR + "/media/")
	mediadir = os.listdir()
	mediafiles = len(mediadir)
	jsonbar = Bar('Processing', max=mediafiles)
	for i in range(mediafiles):
		for filename in os.listdir("."):
			exifoutputjson = exif.get_json(filename)
			#basejson = os.path.basename(filename)
			os.chdir(ROOT_DIR + "/exifdata/json")
			#Prints output to json file
			print(json.dumps(exifoutputjson, sort_keys=True, indent=0, separators=(',', ': ')), 
				file= open(filename + ".json","w"))
			#print(json.dumps(exifoutputjson, sort_keys=True, indent=0, separators=(',', ': ')), 
			#	file= open(os.path.splitext(basejson)[0]+".json","w"))

			jsonbar.next()
			os.chdir(ROOT_DIR + "/media")	
		break
	jsonbar.finish()

def exifHTML():
	"""
	Extract metadata from files and output as HTML format.
	Progress bar indicates processing status.
	"""
	print("Running exiftool to HTML")
	os.chdir(ROOT_DIR + "/media/")
	mediadir = os.listdir()
	mediafiles = len(mediadir)
	htmlbar = Bar('Processing', max=mediafiles)
	for i in range(mediafiles):
		for filename in os.listdir("."):
			#Prints output to HTML
			#basehtml = os.path.basename(filename)
			exifoutputhtml = exif.command_line(['exiftool', '-h', filename])
			os.chdir(ROOT_DIR + "/exifdata/html")
			#print(exifoutputhtml,file = open(os.path.splitext(basehtml)[0]+ ".html", "w"))
			print(exifoutputhtml,file = open(filename + ".html","w"))
			htmlbar.next()
			os.chdir(ROOT_DIR + "/media")
		break
	htmlbar.finish()

def exifHTMLDump():
	"""
	Extract hexadecimal dump of file metadata and output as HTML.
	Useful for deep binary analysis and forensic examination.
	"""
	print("Running exiftool to HTML Dump")
	os.chdir(ROOT_DIR + "/media/")
	mediadir = os.listdir()
	mediafiles = len(mediadir)
	os.chdir(ROOT_DIR + "/media/")
	htmldumpbar = Bar('Processing', max=mediafiles)
	for i in range(mediafiles):
		for filename in os.listdir("."):
			#basehtmldump = os.path.basename(filename)
			exifoutputhtmldump = exif.command_line(['exiftool', '-htmlDump', filename])
			os.chdir(ROOT_DIR + "/exifdata/hex_html")	
			#htmldumpfile = open(os.path.splitext(basehtmldump)[0] + ".html", 'wb')
			htmldumpfile = open(filename + ".html", 'wb')
			htmldumpfile.write(exifoutputhtmldump)
			htmldumpfile.close()
			htmldumpbar.next()
			os.chdir(ROOT_DIR + "/media")
		break
	htmldumpbar.finish()	
