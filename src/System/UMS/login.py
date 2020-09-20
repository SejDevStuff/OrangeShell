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

# ---- import dependencies -----
import os	# os, time and sys are auto installed
import time
import sys
from __main__ import ROOT_DIR, EncryptHomeStatus
try:
	import hashlib		# hashlib, getpass and colorama must be installed by user, throw error if not exist.
	import getpass
	from colorama import init, Fore, Back, Style
	init(convert=True)
	import zipfile
except Exception as e:
	print(str(e))
	sys.exit(0)
timeout_seconds = 0
# ------------------------
def timeout():
	global timeout_seconds
	tm_value = timeout_seconds
	try:
		while tm_value > 0:
			print(Fore.RED + Style.BRIGHT + "Error: You have had three wrong attempts, please wait " + str(tm_value) +" seconds before retrying... Press CTRL+C now if you wish to exit" + Style.RESET_ALL, end="\r")
			tm_value -= 1
			time.sleep(1)
		if tm_value == 0:
			print("\n")
			return login()
	except KeyboardInterrupt:
		sys.exit(0)
def loginUsernameProvided(username):		# Used in the LOCK feature, login but with the username already provided (so only ask for pass)
	global timeout_seconds
	wrong_attempts = 0
	ask = True
	try:
		while ask: # Keep letting user retry until they get it right.
			password = getpass.getpass(str(username) + "'s Password? ") # PSW PROMPT
			print('Validating ...')
			if os.path.exists(ROOT_DIR + '/UMS/' + username + '.shadow'): # Where user passwords are stored, hashed.
				passw = password.encode('utf8') # Encode input with utf8
				hash_object = hashlib.sha512(passw) # Hash input
				hex_dig = hash_object.hexdigest()
				f = open(ROOT_DIR + '/UMS/' + username + '.shadow', 'r') # Get real hash from file
				actual_pass = f.readline()
				f.close()
				if hex_dig == actual_pass: # If input hash == real hash, correct psw
					os.system('clear')
					if password == "orangeshell":
						print(Style.BRIGHT + Fore.YELLOW + 'Your password is the default OrangeShell password. Consider changing it using change_pswd.' + Style.RESET_ALL) # Warn user if psw is "OrangeShell"
					return username, password
				else:
					time.sleep(5) # deter brute force attacks
					print(Style.BRIGHT + Fore.YELLOW + 'Authentication Error! Try again.' + "\n" + Style.RESET_ALL)
					wrong_attempts += 1
					if wrong_attempts == 3:
						timeout_seconds += 5
						ask = False
						return timeout()
			else:
				time.sleep(5) # deter brute force attacks
				print(Style.BRIGHT + Fore.YELLOW + 'Authentication Error! Try again.' + "\n" + Style.RESET_ALL)
				wrong_attempts += 1
				if wrong_attempts == 3:
					timeout_seconds += 5
					ask = False
					return timeout()
	except KeyboardInterrupt: # if ctrl+c pressed, exit as tamper alert.
		print('Authentication Error! This function does not support try-again so exiting...')
		sys.exit(0)

# HERE IT IS BASICALLY THE SAME PRINCIPLE AS ABOVE BUT IT ASKS FOR USERNAME TOO
def login():
	global timeout_seconds
	wrong_attempts = 0
	ask = True
	try:
		while ask:
			username = input('Username? ')
			password = getpass.getpass(str(username) + "'s Password? ")
			print('Validating ...')
			if os.path.exists(ROOT_DIR + '/UMS/' + username + '.shadow'):
				passw = password.encode('utf8')
				hash_object = hashlib.sha512(passw)
				hex_dig = hash_object.hexdigest()
				f = open(ROOT_DIR + '/UMS/' + username + '.shadow', 'r')
				actual_pass = f.readline()
				f.close()
				if hex_dig == actual_pass:
					if EncryptHomeStatus == "YES":
						if not os.path.isdir(ROOT_DIR + '/../' + username):
							print('Decrypting home directory.')
							HOMELOCd = ROOT_DIR + '/../' + username + '.enc'
							if not os.path.isfile(HOMELOCd):
								print('Fail --> ENC file doesnt exist.')
								if password == "orangeshell":
									print(Style.BRIGHT + Fore.YELLOW + 'Your password is the default OrangeShell password. Consider changing it using change_pswd.' + Style.RESET_ALL)
								return username, password
							else:
								try:
									
									HOMELOC = os.getcwd() + '/../'
									os.chdir(HOMELOC)
									os.system('7z x ' + HOMELOCd + ' -p"'+ password +'" -y > /dev/null')
									if os.path.isdir(HOMELOC + username):
										print('Success!')
										os.system('rm '+ username +'.enc')
										if password == "orangeshell":
											print(Style.BRIGHT + Fore.YELLOW + 'Your password is the default OrangeShell password. Consider changing it using change_pswd.' + Style.RESET_ALL)
										return username, password
									else:
										print('Fail! Continuing anyway...')
										if password == "orangeshell":
											print(Style.BRIGHT + Fore.YELLOW + 'Your password is the default OrangeShell password. Consider changing it using change_pswd.' + Style.RESET_ALL)
										return username, password
								except Exception as e:
									print('Fail ('+ str(e) +'). Continuing anyway...')
									if password == "orangeshell":
										print(Style.BRIGHT + Fore.YELLOW + 'Your password is the default OrangeShell password. Consider changing it using change_pswd.' + Style.RESET_ALL)
									return username, password
						else:
							print('Resuming...')
							if password == "orangeshell":
								print(Style.BRIGHT + Fore.YELLOW + 'Your password is the default OrangeShell password. Consider changing it using change_pswd.' + Style.RESET_ALL)
							return username, password
					else:
						print('Home encryption was disabled in shellconfig.txt. Resuming without it.')
						return username, password
				else:
					time.sleep(5)
					print(Style.BRIGHT + Fore.YELLOW + 'Authentication Error! Try again.' + "\n" + Style.RESET_ALL)
					wrong_attempts += 1
					if wrong_attempts == 3:
						timeout_seconds += 5
						ask = False
						return timeout()

			else:
				time.sleep(5)
				print(Style.BRIGHT + Fore.YELLOW + 'Authentication Error! Try again.' + "\n" + Style.RESET_ALL)
				wrong_attempts += 1
				if wrong_attempts == 3:
					timeout_seconds += 5
					ask = False
					return timeout()

	except KeyboardInterrupt:
		print('Authentication Error! This function does not support try-again so exiting...')
		sys.exit(0)
