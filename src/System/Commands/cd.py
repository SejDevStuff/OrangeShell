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
from __main__ import UserAcc, ROOT_DIR
# main file
def shellexec(cmddir):
	dir = cmddir.strip()
	if dir == "": # if no args go back to homedir
		os.chdir(ROOT_DIR + '/../' + UserAcc)
		return
	if os.path.isdir(dir): # make dir change if dir exists
		os.chdir(dir)
	else:
		print('Error: '+ str(dir) +' is not a directory or does not exist.') # dir doesnt exist
		return
