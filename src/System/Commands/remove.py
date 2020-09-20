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

# removefile
def removeFile(INPUT):
	print('Removing source file "'+str(INPUT)+'"')
	os.system('rm '+ str(INPUT))  # remove file using command
	
# removedir
def removeDir(INPUT):
	print('Removing entire source directory "'+str(INPUT)+'"')
	os.system('rm -rf ./'+ str(INPUT) + '/') # remove entire dir

# shellexec
def shellexec(cmdINPUT):
	INPUT = cmdINPUT.strip() # remove leading and trailing whitesace
	if INPUT == "": # missing args, throw err
		print('E: Missing argument for REMOVE: INPUT_FILE')
	if os.path.exists(INPUT): # if input exists...
		if os.path.isdir(INPUT): # if input is dir...
			print('Removing directory `'+ str(INPUT) +'`')
			removeDir(INPUT) # call removedir
		else:
			print('Removing file `'+ str(INPUT) +'`')
			removeFile(INPUT) # else call removefile
	else:
		print('Error: Input file `'+ str(INPUT) +'` does not exist.') # input doesnt exist, throw err
