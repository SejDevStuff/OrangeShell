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
import os
import sys

# try and get version args
try:
	Version = sys.argv[2]
except: # cannot get ver args, probs the user executed the file directly.
	print('This command cannot be run directly! Please use the "update" command in the shell to launch the update manager.')
	sys.exit()

# UPDATE 
print('Welcome to the OrangeOS Update Wizard!')
VERIFY_START = input('Do you want to update OrangeOS to the latest version? Your user files will not be affected, but you may need to set a password again! Y/N: ') #ask for verif
if VERIFY_START == "y" or VERIFY_START == "Y":  # if user said "y" or "Y"...
	print('Starting the update...') # start update. 
else: # else...
	print('Abort.') # ABORT
	sys.exit()
try:
	import requests # try and import requests
except:
	print('OrangeOS.Main.UpdateManager.Error.MissingComponentError: Component "requests" is missing and is needed to run OrangeOS Update Manager') # cannot import requests
print('=> Checking for updates ...')
try:
	orangeosver = requests.get('https://87ferrets.ml/SystemFetchArchive/OrangeOS/LV_STRING.INFO') # get Latest Version String
	VERSTRING = orangeosver.text.strip()
	if VERSTRING == Version: # if versionstring from file is the same as the version argument passed, the system is up to date and no need to update
		print('There is no need for an update! Aborting...')
		sys.exit(0)
	else:
            print('An update is available. You are using OrangeShell v' + str(Version) + ' but an update to OrangeShell v' + str(VERSTRING) + ' is available.') # else an update is available.
except:
	print('OrangeOS.Main.UpdateManager.Error.RequestFailedError: The request to the remote server failed. Cannot continue update.') # could not contact server
	sys.exit()

ynS = input('Do you want to update? y/n: ')
if ynS == "y" or ynS == "Y":
    print('Starting the update!')
else:
    print('Abort!')
    sys.exit(0)

print('SKIPPING USER FILES!')
print('==> Making backup of System...')
os.chdir('..')
def copyDir(INPUT, OUTPUT):
	print('Copying entire source directory "'+str(INPUT)+'" to destination "'+str(OUTPUT)+'"')
	os.system('cp -r '+ str(INPUT) +' '+ str(OUTPUT)) 
System_Dir = os.getcwd() + '/System'
copyDir(System_Dir, System_Dir + '.BACKUP/')	# make entire backup of system
print('Verifying backup...')
if os.path.isdir(System_Dir + '.BACKUP/'): # verify backup exists
	print('Backup Exists!')
else:
	print('OrangeOS.Main.UpdateManager.Error.ProcessError: Backup failed. Cannot continue as it is too dangerous.') # else backup doesnt exist, exit!
	sys.exit()
print('=> Deleting old system directory...')
os.system('rm -rf '+ System_Dir + '/') # delete System directory 
print('=> Getting new system package from server...') # get pkg from server
def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)
try:
	download_url("https://87ferrets.ml/SystemFetchArchive/OrangeOS/System.zip","System.zip") # get system.zip from server
except:
	print('OrangeOS.Main.UpdateManager.Error.RequestFailedError: The request to the remote server failed. Cannot continue update.')# cannot get.
	print('A fail was detected! Restoring from backup...') # restore backup
	os.system('mv System.BACKUP System')
	if os.path.isdir(System_Dir):
		print('Restored! Exiting...')
		sys.exit() # restored
	else:
		print('Oh dear!! Something went wrong and the backup could not be restored! Please re-install OrangeOS. Your user files should be untouched but you may have to re-create a new account.')
		sys.exit() # FAILED TO RESTORE!
try:
	import zipfile # try and import zipfile
except:
	print('OrangeOS.Main.UpdateManager.Error.MissingComponentError: Component "zipfile" is missing and is needed to run OrangeOS Update Manager') # cannot import
	print('A fail was detected! Restoring from backup...') # restore
	os.system('mv System.BACKUP System')
	if os.path.isdir(System_Dir):
		print('Restored! Exiting...')
		sys.exit() # restore
	else:
		print('Oh dear!! Something went wrong and the backup could not be restored! Please re-install OrangeOS. Your user files should be untouched but you may have to re-create a new account.')
		sys.exit() # FAILED TO RESTORE!!
try:
	with zipfile.ZipFile("System.zip", 'r') as zip_ref:
		zip_ref.extractall(os.getcwd()) # try and unzip system file
except:
	print('OrangeOS.Main.UpdateManager.Error.FileExtractionError: Could not extract System.zip file!') # cannot
	print('A fail was detected! Restoring from backup...') # restore backup
	os.system('mv System.BACKUP System')
	if os.path.isdir(System_Dir):
		print('Restored! Exiting...')
		sys.exit() # restored
	else:
		print('Oh dear!! Something went wrong and the backup could not be restored! Please re-install OrangeOS. Your user files should be untouched but you may have to re-create a new account.')
		sys.exit() # cannot restore
print('The upgrade was completed. ') # complete
print('Removing backup...') 
os.system('rm -rf '+ System_Dir + '.BACKUP/') # rm backup
print('Removing temporary archive...')
os.system('rm System.zip') # rm system.zip file
print(' ====> On the first boot the user setup will launch which will help you set up OrangeOS even further by creating User Accounts that were present in an older installation. <====')
print('All done!') # done!
