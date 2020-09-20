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

# import dependencies
import os

# movefile command
def moveFile(INPUT, OUTPUT):
	print('Moving source file "'+str(INPUT)+'" to destination "'+str(OUTPUT)+'"')
	os.system('mv '+ str(INPUT) +' '+ str(OUTPUT)) # move input to output
	
# movedir command
def moveDir(INPUT, OUTPUT):
	print('Moving entire source directory "'+str(INPUT)+'" to destination "'+str(OUTPUT)+'"')
	os.system('mv '+ str(INPUT) +' '+ str(OUTPUT)) # move input to output
	
# shellexec
def shellexec(cmdMASHED_ARGS):
	MASHED_ARGS = cmdMASHED_ARGS.strip() # remove leading and trailing whitspace
	# Split MASHED_ARGS into INPUT and OUTPUT
	SPLIT_ARGS = MASHED_ARGS.split() # make array out of mashed args
	if len(SPLIT_ARGS) < 2 or len(SPLIT_ARGS) > 2: # wrong number of args passed, if args is under 2 or over 2, it must be 2 exactly - input and output
		print('Error: Invalid number of arguments passed to command. Exiting...')
		return
	INPUT_FILE = SPLIT_ARGS[0] # get inputfile
	OUTPUT_FILE = SPLIT_ARGS[1] # get outputfile
	if os.path.exists(INPUT_FILE): # if input exists...
		if os.path.isdir(INPUT_FILE): # if input is dir...
			print('Moving directory `'+ str(INPUT_FILE) +'`')
			moveDir(INPUT_FILE, OUTPUT_FILE) # call movedir
		else:
			print('Moving file `'+ str(INPUT_FILE) +'`')
			moveFile(INPUT_FILE, OUTPUT_FILE) # else call movefile
	else:
		print('Error: Input file `'+ str(INPUT_FILE) +'` does not exist.') # input file doesnt exist
