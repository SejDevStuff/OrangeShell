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
from __main__ import *
try:
	from colorama import init, Fore, Back, Style
	init(convert=True)
except Exception as e:
	print('Exception error whilst initilaising program! Details: '+ str(e))

def shellexec(spill_random):
	os.system('clear') # clear screen
	print(Style.BRIGHT + Fore.GREEN + "This shell is locked! "+ str(UserAcc) +" is logged in. Press any key to unlock!" + Style.RESET_ALL) # say in green text shell is locked
	os.system('read') # wait for keypress
	try:
		sys.path.insert(1, ROOT_DIR + '/UMS') # try and import login
		login_system = importlib.import_module('login') # import login
		US_ACC = login_system.loginUsernameProvided(UserAcc) # use loginUsernameProvided function explained in login.py
	except Exception as e: # cannot get to login, store exception in var e and print err below:
		print('E: An error occurred with contacting the login system.') 
		print('EXCEPTION DETAILS: '+ str(e))
		sys.exit(0)
	return
