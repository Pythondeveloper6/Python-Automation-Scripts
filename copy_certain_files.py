# Selective copy

'''Walking through a folder tree and searching for files with a certain file extension('.jpg','.pdf')
 and copying from whatever location they are present at to a new folder'''

 import shutil

 import os

 # Walking through a folder tree
 os.makedirs('newfolder', exist_ok=True)

 for folders,subfoldes,filenames in os.walk('.'):
 	for filename in filenames:
 		if filename.endswith('.jpg') or filename.endswith('.pdf'):
 			shutil.copy(file_name,'newfolder')
 			
