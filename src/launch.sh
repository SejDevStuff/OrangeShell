#!/bin/bash

if [[ $1 == "--override-checks" || $2 == "--override-checks" ]]; then
  echo "Overriding checks for p7zip-full..."
  OVERRIDE="y"
fi
if [[ $1 == "--backup-fail-override" || $2 == "--override-checks" ]]; then
  echo "Overriding failed backup precautions..."
  BACKUP_FAIL_OVERRIDE="y"
fi

if test -f $(pwd)/SystemBackup.tar.gz; then
  echo "WARNING! You do not have a system backup! This means if your system breaks you have nothing to go to! Making one now..."
  tar -cvf $(pwd)/SystemBackup.tar.gz $(pwd)/System/*
  if test -f $(pwd)/SystemBackup.tar.gz; then
    echo "Backup made successfully."
  else
    if [[ $BACKUP_FAIL_OVERRIDE == "y" ]]; then
      echo "Backup failed, but overriding exit. WARNING! Be careful you do not have a backup anymore."
    else
      echo "The backup failed. Continuing is DANGEROUS. So I will exit, use --backup-fail-override to override this precaution."
      exit
    fi
fi

if [[ $OVERRIDE != "y" ]]; then
  echo -e "\nThis currently only works for distros that use 'dpkg' and 'apt', if you do not use any of these bewarned some stuff may not work"
  echo -e "Use --override-checks argument to override this if you know you have the package and are using a different package manager"
fi
echo -e "\nSleeping for 5 seconds..."
sleep 5

no_encrypt() {
  DATE=`date +"%d-%b-%Y"`
  if test -f "./System/shellconfig.old"; then
    BACKUP_NAME="./System/shellconfig.old.$DATE"
  else
    BACKUP_NAME="./System/shellconfig.old"
  fi
  echo -e "\nEncryption is disabled due to the lack of encryption software. \nRewriting shellconfig to match this. \nNOTE: A backup will be saved as $BACKUP_NAME"
  cp "./System/shellconfig.txt" "$BACKUP_NAME"
  echo "
  # Sentences beginning with a hashtag (\"#\") is considered a comment and will be ignored.
  # You may wish to uncomment configuration values if you are certain it wont break your
  # system by putting a hashtag and a space (\"# \") in front of them

  # Shell configuration file for OrangeShell

  # IN THIS SECTION, THE STATES ARE EITHER \"YES\" or \"NO\", CAPITILAZATION DOES MATTER!
  # Once the shell is started, the values here are set until you restart the shell.

  # check for updates on startup
  # it is reccommended to check if you want to stay updated on security and feature updates!
  CheckForUpdates = YES

  # Encrypting your home directory.

  # Error: You do not have proper software to encrypt your home directory so it is disabled

  EncryptHome = NO

  # Remove OrangeSH_Cache folder on exit.
  # YES ==> The cache folder will be removed so it will save you space (it respawns on restart of OrangeShell)
  # NO ==> The cache will not be removed, this may be handy if you experience errors often and want to check logs in the cache
  RemoveCache = YES" > ./System/shellconfig.txt
}

echo "Starting shell..."
if [[ $OVERRIDE != "y" ]]; then
  echo -e "\np7zip-full must be installed to use encryption. Checking for that now..."

  if ! dpkg-query -l p7zip-full > /dev/null; then
    echo -e "p7zip-full not found! \nEnter sudo password to install, else press CTRL+C to cancel."
      sudo apt-get install p7zip-full
      echo -e "\nRechecking..."
      if ! dpkg-query -l p7zip-full > /dev/null; then
        no_encrypt
      fi
  else
      echo -e "\np7zip-full Installed!"
  fi
fi

if test -f $(pwd)/System.tar.gz; then
  echo "Decompressing system..."
  tar -xvf $(pwd)/System.tar.gz
  if [ -d $(pwd)/System/ ]; then
    echo "Decompressing went well!"
    rm $(pwd)/System.tar.gz
  else
    echo "** Something went wrong with decompressing!"
    if test -f SystemBackup.tar.gz; then
      echo "YOU HAVE A BACKUP! Please restore from that if things look bad..."
    else
      echo "Sadly you do not have a backup, please re-install OrangeShell"
    fi
  fi
fi

echo -e "\nLaunching shell!"
cd System
python3 shell.py

echo "Compressing system..."

if test -f $(pwd)/System.tar.gz; then
  echo "System seems to be already compressed. Skipping!"
else
  tar -cvf $(pwd)/System.tar.gz $(pwd)/System/*
  if test -f $(pwd)/System.tar.gz; then
    echo "Compression went well."
    rm -rf $(pwd)/System/
  else 
    echo "** Something went wrong with compressing!"
  fi
fi