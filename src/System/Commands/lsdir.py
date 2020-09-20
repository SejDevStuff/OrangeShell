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
import os
import sys
import time

def lsdir(input):
	print("Directory listing for: " + str(input))
	COL1TITLE = "[File Type]"
	COL2TITLE = "[File Name]"
	print("\n{0:30}  {1}".format(COL1TITLE, COL2TITLE))
	total = 0
	for entry in os.scandir(input):
		total += 1
		if os.path.isdir(entry):
			TYPE = "Directory"
		else:
			EXT_TUPLE = os.path.splitext(entry.path)
			EXT = EXT_TUPLE[1]
			if EXT != "":
				TYPE = str(EXT) + ' File'
			else:
				TYPE = "Unknown File"
		print("{0:30}  {1}".format(TYPE, entry.path))
	print("")
	print('Total top-level files and directories in "' + str(input) +'" is ' + str(total))

def shellexec(cdirname):
	dirname = cdirname.strip()
	if dirname == "":
		print('Missing argument: DIRECTORY')
		return
	if os.path.isdir(dirname):
		lsdir(dirname)
	else:
		print('Error: "' + str(dirname) + '" is not a directory.')
