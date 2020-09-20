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
import time
from __main__ import UserAcc, ROOT_DIR # get dynamic root and useracc


def shellexec(cmdusername):
	try:
		import hashlib # try to import hashlib
		import getpass # try to import getpass
	except:
		print('E: Missing dependencies, hashlib or getpass.') # throw err, one is not installed
		return
	username = cmdusername.strip() # remove leading and trailing whitespace
	if username == UserAcc: # if requested removal user is yourself...
		print('E: You cannot remove yourself.') # throw err.
		return
	if username == "": # if username argument is nothing...
		print('E: Missing argument, "USERNAME"') # throw err.
		return
	if os.path.isfile(ROOT_DIR + '/UMS/'+ username +'.shadow'): # check if shadow file for usr exists, essentially check if user exists
		verify = input('Do you really want to remove '+ str(username) +'? Y/n: ') # ask if they want to remove
		if verify == "y" or verify == "Y":
			password = getpass.getpass("Existing password for "+ str(username) +"? ") # get psw to verify
			print('Validating ...')
			passw = password.encode('utf8') # encode input using utf8
			hash_object = hashlib.sha512(passw) # hash encoded input
			hex_dig = hash_object.hexdigest() # digest hash
			f = open(ROOT_DIR + '/UMS/' + username + '.shadow', 'r') # open shadow file
			actual_pass = f.readline() # get real hash
			f.close()
			if hex_dig == actual_pass: # if input hash == real hash
				print('Validation Successful.')
				print('Removing user entry...')
				os.system('rm ' + ROOT_DIR + '/UMS/'+ username +'.shadow')
				print('Checking for home directory...')
				if os.path.isdir(ROOT_DIR + '/UMS/' + username): # if home dir exists...
					print('Removing home directory ...')
					os.system('rm -rf '+ ROOT_DIR + '/UMS/' + username) # delete home dir
				else:
					print('Home directory does not exist. Ignoring.')
				print('Operation complete.') # done!
			else:
				time.sleep(5)
				print('Sorry that is not correct.') # password not correct
				return
		else:
			print('Operation aborted.')	# aborted operation
	else:
		print('User "'+ str(username) +'" does not exist!') # user does not exist
		print('Aborting ...')
