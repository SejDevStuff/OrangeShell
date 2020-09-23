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
import os
import sys
ROOT_DIR = os.getcwd()
def makeUser(username):
	try:
		import hashlib # import hashlib (try to)
		import getpass # import getpass (try to)
	except:
		print('E: Missing dependencies, hashlib or getpass.') # cannot import, show err
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
def setup():
	print("Hi! Nice to have you here. Let's setup OrangeShell for the first time for you.")
	print('We must set up a user account for you, so press any key to start the process.')
	os.system('read')
	print('')
	print('==> Setup is auto detecting any user accounts from the previous installation of OrangeShell ...')
	rootdir = os.getcwd() + '/../'
	total = 0
	for entry in os.scandir(rootdir):
		if os.path.isdir(entry.path):
			dirname = entry.path.replace(os.getcwd() + '/../','')
			if dirname == "System":
				needed = 'no'
			elif dirname == "UpdateManager":
				needed = 'no'
			else:
				total += 1
				print('')
				print('Setup has detected this possible user home directory. I am going to analyse deeper...')
				print('Possible user directory: "' + dirname + '"')
				print('Analysing situation...')
				if os.path.isfile(os.getcwd() + '/UMS/' + str(dirname) + '.shadow'):
					print('This user already seems to have a user entry for the login system so I am skipping this user.')
				else:
					print('This user does not seem to have a user entry for the login system, do you want me to make one?')
					yn2 = input('Y/n: ')
					if yn2 == "y" or yn2 == "Y":
						print('Alright... making a user entry!')
						rate = makeUser(dirname)
					else:
						print('Seems like you aborted. Skipping user...')
		else:
			needed = 'no'
	if total == 0:
		print('Setup did not find any user home directories. Skipping this step...')
	else:
		print('')
		print('User setup is complete!')
	print('Remember, if you did not set up a user, you can always log in with the default user account and use the command "mkusr" to make a new user.')
	print('Default account details:')
	print('USERNAME = default')
	print('PASSWORD = orangeshell') 
	print('')
	print('==> Setup will now guide you through OrangeShell...')
	print('')
	print('Right! Last thing before we part ways... have you read the changelog? It is important! If not, I can show you!')
	yn4 = input('Y/n: ')
	if yn4 == "n" or yn4 == "N":
		print('That is a no to me! Just a sec and I will show you... by the way, just close the file when you finished and I will move on.')
		if os.path.isfile('changelog.pdf'):
			print('Starting CHANGELOG file')
			os.system('changelog.pdf')
		else:
			print(':( No changelog file found! You can always get it yourself from the OrangeShell FTP space at https://87ferrets.ml/FTP/OrangeOS !')
	print('')
	print('DONE! You are ALL SET for OrangeShell!! Just a FEW things before you can properly use it.')
	print('')
	print('I hope you remember your user credentials to log in, or you will be locked out!')
	print('')
	print('I hope you find OrangeShell pleasant. Remember, the "help" command is there if you need any help.')
	print('Press any key to exit, it is time to part ways!')
	os.system('read')
	print('')
	print('Self destructing...')
	os.remove("user_setup.pyc")
	sys.exit(0)
		
