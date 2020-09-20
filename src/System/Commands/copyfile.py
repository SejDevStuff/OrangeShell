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

# Copyfile function
def copyFile(INPUT, OUTPUT):
	print('Copying source file "'+str(INPUT)+'" to destination "'+str(OUTPUT)+'"')
	os.system('cp '+ str(INPUT) +' '+ str(OUTPUT)) # copy source to destination using windows copy cmd
	
# copydir function
def copyDir(INPUT, OUTPUT):
	print('Copying entire source directory "'+str(INPUT)+'" to destination "'+str(OUTPUT)+'"')
	os.system('cp -avr '+ str(INPUT) +' '+ str(OUTPUT)) # copy entire directory to destination using windows xcopy cmd
	
# main shell
def shellexec(cmdMASHED_ARGS):
	MASHED_ARGS = cmdMASHED_ARGS.strip() # remove leading and trailing whitespace
	# Split MASHED_ARGS into INPUT and OUTPUT
	SPLIT_ARGS = MASHED_ARGS.split()
	if len(SPLIT_ARGS) < 2 or len(SPLIT_ARGS) > 2: # invalid number of args
		print('Error: Invalid number of arguments passed to command. Exiting...')
		return
	INPUT_FILE = SPLIT_ARGS[0] # get input
	OUTPUT_FILE = SPLIT_ARGS[1] # get output
	if os.path.exists(INPUT_FILE): # does source exist? if so...
		if os.path.isdir(INPUT_FILE): # check if source is dir
			print('Copying directory `'+ str(INPUT_FILE) +'`') # if dir, copy using copydir
			copyDir(INPUT_FILE, OUTPUT_FILE)
		else:
			print('Copying file `'+ str(INPUT_FILE) +'`') # else copy using copyfile
			copyFile(INPUT_FILE, OUTPUT_FILE)
	else:
		print('Error: Input file `'+ str(INPUT_FILE) +'` does not exist.') # source doesnt exist
