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
from __main__ import ROOT_DIR

# shellexec
def shellexec(cmdusername):
	try:
		import hashlib # import hashlib (try to)
		import getpass # import getpass (try to)
	except:
		print('E: Missing dependencies, hashlib or getpass.') # cannot import, show err
		return
	username = cmdusername.strip() # remove leading and trailing whitespace
	if username == "": # no args passed show err
		print('Missing argument: USERNAME')
		return
	if os.path.isfile(ROOT_DIR + '/UMS/'+ username +'.shadow'): # if user shadow file exists...
		print('E: User "'+ username +'" exists!') # throw err and return
		return
	pswd = getpass.getpass('Password for ' + str(username) + '? ') # ask for a password
	test_pswd = pswd.strip() # remove leading and trailing whitspace ONLY FOR A TEST, spaces in real psw will be maintained
	if test_pswd == "": # test if psw is blank, if yes, throw err
		print('E: Password cannot be blank.')
		return
	vpswd = getpass.getpass('Verify password for ' + str(username) + ': ') # verify psw
	if pswd == vpswd: # if psw entered is verified correctly
		print('Making user entry ...') # mk usr entry
		passw = pswd.encode('utf8') # encode password input
		hash_object = hashlib.sha512(passw) # hash psw
		hex_dig = hash_object.hexdigest() # digest hash
		f = open(ROOT_DIR + '/UMS/' + username + '.shadow', 'w+') # make shadow file
		f.write(hex_dig) # write hash to file
		f.close() # exit
		if os.path.isdir(ROOT_DIR + '/../' + username): # if home dir exists, skip.
			print('Home directory exists. Skipping step...')
		else: # else make one.
			print('Making home directory ...')
			os.system('mkdir -p ' + ROOT_DIR + '/../' + username)
		print('Operation Completed')
	else:
		time.sleep(5)
		print("Sorry, that wasn't correct.") # verify psw was incorrect, throw err.
		return
	
