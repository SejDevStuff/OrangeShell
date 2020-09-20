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
import sys
from __main__ import ROOT_DIR
# shellexec 
def shellexec(cmd_command):
	try:
		import requests # try to import requests
	except:
		print('Missing component: requests') # if it cannot import, throw err
		return
	command = cmd_command.strip() # remove leading or trailing whitespace
	if command == "": # no args, throw err
		print('What do you need help with? For example: "help --listall" will list all commands and "help help" will show the help documentation for help.')
		return
	if command == "--listall": # listall arg was given
		print('Gathering command information...')
		all_cmd_list = open(ROOT_DIR + '/helpdb/ALL_CMD.list',"r")
		for line in all_cmd_list:
			print(line.strip())
		all_cmd_list.close()
		return
	else:
		print('Searching for a help file for that command...')
		try:
			helpdoc = open(ROOT_DIR + '/helpdb/' + str(command) + '.helpfile')
			print('Showing help documentation for: '+ str(command) + "\n") 
			for line in helpdoc:
				print(line.strip())
			helpdoc.close()
			print('')
		except:
			print('Oh dear! I cannot find help documentation for "'+ str(command) +'". Did you check your syntax properly?')
		return
