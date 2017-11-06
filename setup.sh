#!/bin/bash
clear

# removing the file extension
newFileName=`echo $1 | cut -d "." -f1`

# verify argument
if [ $# -eq 0 ]
then
  echo "[-] Error! Missing Argument..."
  exit 1
fi

# verify privileges
if [ $UID != 0 ]
then
  echo "[-] Root privileges needed..."
  echo "[-] Exiting..."
  exit 1
fi

# copying script to desired destination
echo "[*] Copying $1 to /bin/ ..."
cp $1 /bin/

if [ $? -eq 0 ]
then
  echo "[+] Successfully copied $1 to /bin/ ..."
  echo "[*] Removing the file extension..."
  mv /bin/$1 /bin/$newFileName
  echo "[*] Setting execution bit..."
  chmod +x /bin/$newFileName
  if [ $? -eq 0 ]
  then
    echo "[+] $newFileName is executable..."
    exit 0
  else
    echo "[-] Error! Setting X bit failed..."
    echo "[-] Exiting..."
    exit 1
  fi
else
  echo "[-] Error! Copy process failed..."
  exit 1
fi
