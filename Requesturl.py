print('    S57 - Python - Request- URL')
print('    by @s57cyber https://github.com/s57cyber')
print("Disclaimer. This repository is for research purposes only, the use of this code is your responsibility. I take NO responsibility ... AT YOUR OWN RISK. Once again, ALL files available here are for EDUCATION and/or RESEARCH purposes ONLY.")
print("----------------------------------------------------")
"\n\n"

#!usr/bin/env python

import requests
import os

# 	for large file in chunk
#	Get the link or url
#url = 'demo.exe'

#r = requests.get(url, stream=True)

#with open("demo.exe", "wb") as Pypdf:

#	for chunk in r.iter_content(chunk_size = 1024):

#		if chunk:

#			Pypdf.write(chunk)


url = 'https://s57.in/wp-content/uploads/2020/05/s57-png.png'
r = requests.get(url, allow_redirects=True)

#Save the content with name.
open('logo.png', 'wb').write(r.content)

#running File
os.startfile("logo.png")
