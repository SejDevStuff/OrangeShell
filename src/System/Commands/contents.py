#    Copyright (C) 2020 OrangeShell Developers
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    See https://www.gnu.org/licenses/ for a copy of the GNU GPL License
#
# 	 The ORANGEShell Repo can be found here: https://87ferrets.ml/FTP/OrangeShell/

# ---- IMPORT DEPENDENCIES ----
import os
import sys

def shellexec(cmdfilename):	# Shellexec file
	filename = cmdfilename.strip()	# Remove leading and trailing whitespace
	if filename == "":
		print('Missing argument: FILENAME')	# Argument missed
		return
	if not os.path.isfile(filename):	# File mentioned does not exist
		if os.path.isdir(filename):		# File is not a file, but a directory
			print('E: Cannot open file for reading. The file `' + str(filename) + '\' is a directory.')
			return
		print('E: Cannot open file for reading. The file `'+ str(filename) + '\' does not exist.')
		return
	totallinenum = len(open(filename).readlines(  ))	# Get total line num
	linenum = 0
	content = ""
	print('Reading line ' + str(linenum) + ' of ' + str(totallinenum) + ' ...', end="\r")	# Dynamic updating line showing how many lines the system read out of total lines
	f = open(filename, "r")
	for line in f:
		linenum += 1
		print('Reading line ' + str(linenum) + ' of ' + str(totallinenum) + ' ...', end="\r") # Edit line as it reads more.
		content += line # Add lines to content
	print("\nThe contents of this file is ready to be displayed. Press any key to display it") 
	os.system('read') # Pause until key pressed
	print("\n" + str(content) + "\n") # SHOW CONTENT
