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
from __main__ import ROOT_DIR, PassW
def overwrite():
	ov_file = open("_.tmp","wb+")
	i = 0
	while i < 10000:
		ov_file.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
		i += 1
	ov_file.close()
	os.system('rm _.tmp')
	print('Done!')

def encryptFile(filename):
	if not os.path.exists(filename):
		print('Error: the file does not exist.')
		return
	print('Encrypting ... (key is tied to your account)')
	os.system('7z a '+ str(filename) +'.enc '+ str(filename) +' -p"' + str(PassW) +'" -y > /dev/null')
	print('Verifying...')
	if not os.path.exists(str(filename) + '.enc'):
		print('Error: the encrypted result could not be made!')
		return
	else:
		print('Success! Deleting shadow...')
		os.system('rm '+ str(filename))
		print('Overwriting 10,000 times...')
		overwrite()

def decryptFile(filename):
	if not os.path.exists(filename):
		print('Error: the file does not exist.')
		return
	print('Decrypting ... (key is tied to your account)')
	os.system('7z x '+ str(filename) +' -p"' + str(PassW) +'" -y > /dev/null')
	print('Verifying...')
	if not os.path.exists(str(filename[:-4])):
		print('Error: could not verify the file exists. Halting!')
		return
	else:
		print('Success! Deleting shadow...')
		os.system('rm '+ str(filename))

def encryptDir(dirname):
	if not os.path.exists(dirname):
		print('Error: the directory does not exist.')
		return
	print('Encrypting ... (key is tied to your account)')
	os.system('7z a '+ str(dirname) +'.enc '+ str(dirname) +'/ -p"' + str(PassW) +'" -y > /dell/null')
	print('Verifying...')
	if not os.path.exists(str(dirname) + '.enc'):
		print('Error: the encrypted result could not be made!')
		return
	else:
		print('Success! Deleting shadow...')
		os.system('rm -rf ./'+ str(dirname) + '/')
		print('Overwriting 10,000 times...')
		overwrite()

def decryptDir(dirname):
	if not os.path.exists(dirname):
		print('Error: the file does not exist.')
		return
	print('Decrypting ... (key is tied to your account)')
	os.system('7z x '+ str(dirname) +' -p"' + str(PassW) +'" -y > /dev/null')
	print('Verifying...')
	if not os.path.exists(str(dirname[:-4])):
		print('Error: could not verify the file exists. Halting!')
		return
	else:
		print('Success! Deleting shadow...')
		os.system('rm -rf ./'+ str(dirname) + '/')
	
def shellexec(MASHED_ARGS):
	STRIPPED_ARGS = MASHED_ARGS.strip()
	if STRIPPED_ARGS == "":
		print('Missing arguments! Mode and Resource. Use "help crypto" to find out how to use this.')
		return
	SPLIT_ARGS = STRIPPED_ARGS.split()
	if len(SPLIT_ARGS) > 2 or len(SPLIT_ARGS) < 2:
		print('Incorrect number of arguments. Use "help crypto" to find out how to use this')
		return
	MODE = SPLIT_ARGS[0]
	RESOURCE = SPLIT_ARGS[1]
	if MODE == "eFile":
		encryptFile(RESOURCE)
	elif MODE == "dFile":
		decryptFile(RESOURCE)
	elif MODE == "dDir":
		decryptDir(RESOURCE)
	elif MODE == "eDir":
		encryptDir(RESOURCE)
	else:
		print('Unknown mode: '+ str(MODE))
		return
	
