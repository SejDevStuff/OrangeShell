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
import sys
import os
from __main__ import UserAcc, PassW, EncryptHomeStatus, ROOT_DIR, RemoveCacheStatus
def shellexec(spill):
	if RemoveCacheStatus == "YES":
		print('Removing Cache...')
		os.system('rm -rf ./' + ROOT_DIR + '/OrangeSH_Cache/')
		if os.path.exists(ROOT_DIR + '/OrangeSH_Cache'):
			print('Cache could not be removed')
		else:
			print('Cache removed')
	else:
		print('RemoveCache is set to NO in shellconfig.txt, so not removing cache.')
	if EncryptHomeStatus == "YES":
		print('Trying to encrypt home directory before exiting... (it will be auto decrypted at login)')
		try:
			HOMEDIR = ROOT_DIR + '/../' + str(UserAcc)
			HOMELOC = ROOT_DIR + '/../'
			if not os.path.isdir(HOMEDIR):
				print('E: Home directory non existent. Exiting...')
				# change dir to root dir
                os.chdir(ROOT_DIR)
                # clear screen
                os.system('clear')
                # spawn new instance of shell
                os.system(ROOT_DIR + '/../launch.sh')
                # exit this shell
                sys.exit(0)
			os.system('7z a '+ HOMELOC + UserAcc + '.enc ' + HOMELOC + UserAcc +'/ -p"' + PassW + '" -y > /dev/null')
			print('Verifying encryption...')
			os.chdir(HOMELOC)
			if os.path.isfile(UserAcc + '.enc'):
				print('Success!')
				os.system('rd /s /q '+ UserAcc)
				overwrite = open('_.tmp',"w+")
				overwrite.close()
				overwrite = open('_.tmp', "a")
				for i in range(1000):
					overwrite.write(str(i) + '-- /x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00/x00')
				overwrite.close()
				os.system('rm _.tmp')
                # change dir to root dir
                os.chdir(ROOT_DIR)
                # clear screen
                os.system('clear')
                # spawn new instance of shell
                os.system(ROOT_DIR + '/../launch.sh')
                # exit this shell
                sys.exit(0)
			else:
				print('Fail!')
				# change dir to root dir
                os.chdir(ROOT_DIR)
                # clear screen
                os.system('cls')
                # spawn new instance of shell
                os.system(ROOT_DIR + '/../launch.sh')
                # exit this shell
                sys.exit(0)
		except Exception as e:
			print('Fail! (' + str(e) +') Exiting...')
			# change dir to root dir
            os.chdir(ROOT_DIR)
            # clear screen
            os.system('cls')
            # spawn new instance of shell
            os.system(ROOT_DIR + '/../launch.sh')
            # exit this shell
            sys.exit(0)
	else:
		print('Home encryption was disabled in shellconfig.txt, exiting anyways.')
		sys.exit(0)
        # change dir to root dir
        os.chdir(ROOT_DIR)
        # clear screen
        os.system('clear')
        # spawn new instance of shell
        os.system(ROOT_DIR + '/../launch.sh')
        # exit this shell
        sys.exit(0)
