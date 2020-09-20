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

# ----- IMPORT DEPENDENCIES -----
from __main__ import *
import os
import time 

# ShellExec Function
def shellexec(spill):
	try:
		import hashlib # IMPORT HASHLIB (or try to)
		import getpass # IMPORT GETPASS (or try to)
	except:
		print('E: Missing dependencies, hashlib or getpass.') # IF NOT INSTALLED, GIVE ERROR
		return
	if os.path.isfile(ROOT_DIR + '/UMS/'+ UserAcc +'.shadow'): 	# Check if user already exists
		password = getpass.getpass("Existing password for "+ str(UserAcc) +"? ") # Ask for existing password
		print('Validating ...') 
		passw = password.encode('utf8') # Encode input into UTF-8
		hash_object = hashlib.sha512(passw) # Hash encoded string with SHA512
		hex_dig = hash_object.hexdigest() # Digest hashed object
		f = open(ROOT_DIR + '/UMS/' + UserAcc + '.shadow', 'r') # Open real shadow file
		actual_pass = f.readline() # Get real hash
		f.close()
		if hex_dig == actual_pass:	# PSW Verification successfull
			print('Validation Successful.')
			pswd = getpass.getpass("New password for "+ str(UserAcc) +"? ")	# Ask for the new password
			test_pswd = pswd.strip() # Remove leading and trailing backspace
			if test_pswd == "":
				print('E: Password cannot be blank.') # Password cannot be blank
				return
			if test_pswd == password:
				print('E: Password cannot be the same pasword you used before!') # Password cannot be same password you entered before
				return
			vpswd = getpass.getpass("Verify new password for "+ str(UserAcc) +": ") # VERIFY PASSWORD
			if pswd == vpswd: # verify password was the same as entered password, continue
				print('Deleting previous entry ...')
				os.system('rm ' + ROOT_DIR + '/UMS/' + UserAcc + '.shadow') # Delete the previous entry
				print('Making new entry ...')
				passw = pswd.encode('utf8')	# Encode new password
				hash_object = hashlib.sha512(passw) # Hash new password
				hex_dig = hash_object.hexdigest()	# Digest hash
				f = open(ROOT_DIR + '/UMS/' + UserAcc + '.shadow', 'w+')	# Open shadow file in overwrite mode
				f.write(hex_dig)	# Overwrite old hash with new hash
				f.close()
				print('Operation Completed.')
				return
			else:
				time.sleep(5)
				print("Sorry, your password doesn't match. Try again later.")	# PSW verify error, return
				return
		else:
			time.sleep(5)
			print('Sorry, authentication error.')	# PSW ERROR, return
			return
	else:
		print('E: User does not exist.')	# User does not exist, throw err, return.
		return
