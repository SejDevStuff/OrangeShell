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

# Import dependencies
import os
import requests
from __main__ import ROOT_DIR, UserAcc
from colorama import Style, init, Fore, Back
import urllib
from urllib.parse import urlparse
from random import randint
init(convert=True)

def download_url(url, save_path, chunk_size=128):
	r = requests.get(url, stream=True)
	with open(save_path, 'wb') as fd:
		for chunk in r.iter_content(chunk_size=chunk_size):
			fd.write(chunk)

# Shellexec file
def shellexec(cmdfile):
	file = cmdfile.strip() # Remove leading and trailing whitespace
	if file == "":
		print('Missing URL!')
		return
	print('Getting status code for URL "' + str(file) +'" ...')
	print('Status Code: ', end="\r")
	try:
		request_response = requests.head(file)
		status_code = request_response.status_code
	except:
		print('Status Code: ?')
		print('The URL you provided seems to point to a server which is non-existent.')
		print('Operation ceased due to status code.')
		return
	if status_code == 200:
		print('Status Code: 200 [OK]')
	else:
		print('Status Code: ' + str(status_code))
		print('Operation ceased due to status code')
		return
	url_parse = urlparse(file)
	requested_file = os.path.basename(url_parse.path)
	if os.path.exists(ROOT_DIR + '/../' + UserAcc):
		if os.path.exists(ROOT_DIR + '/../' + UserAcc + '/' + str(requested_file)):
			requested_file = requested_file + '.' + str(randint(0, 10000))
		print('Saving to your home directory as: '+ str(requested_file))
		download_url(file, ROOT_DIR + '/../' + UserAcc + '/' + str(requested_file))
		if os.path.exists(ROOT_DIR + '/../' + UserAcc + '/' + str(requested_file)):
			print(Fore.GREEN + Style.BRIGHT + 'Success! Your file is saved at ' + ROOT_DIR + '/' + UserAcc + '/' + str(requested_file) + Style.RESET_ALL)
		else:
			print(Fore.YELLOW + Style.BRIGHT + 'Fail! Your file was not saved. Please check for any error output above' + Style.RESET_ALL)
	else:

		# We place the requested file in OrangeSH_Cache if the user does not have a home directory because it is more organised if your files are in one place rather than
		# your files being downloaded everywhere you go and being scattered over the filesystem.

		if not os.path.exists(ROOT_DIR + '/OrangeSH_Cache'):
			os.system('mkdir -p ' + ROOT_DIR + '/OrangeSH_Cache')
		print('Your home directory is non-existent! You should look into the cause of that but your requested file will be saved in "' + ROOT_DIR + '/OrangeSH_Cache".')
		if os.path.exists(ROOT_DIR + '/OrangeSH_Cache/' + str(requested_file)):
			requested_file = requested_file + '.' + str(randint(0, 10000))
		print('Saving file as: ' + str(requested_file))
		download_url(file, ROOT_DIR + '/OrangeSH_Cache/' + str(requested_file))
		if os.path.exists(ROOT_DIR + '/OrangeSH_Cache/' + str(requested_file)):
			print(Fore.GREEN + Style.BRIGHT + 'Success! Your file is saved at ' + ROOT_DIR + '/OrangeSH_Cache/' + str(requested_file) + Style.RESET_ALL)
		else:
			print(Fore.YELLOW + Style.BRIGHT + 'Fail! Your file was not saved. Please check for any error output above' + Style.RESET_ALL)
