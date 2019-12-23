

import os
from PIL import Image


#LOGO_FILENAME = 'catlogo.png'
LOGO_FILENAME = input('Enter The Logo Name With Extension: ')
NEW_FOLDER_NAME = input("Enter The New Folder Name : ")

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs(NEW_FOLDER_NAME, exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
       or filename == LOGO_FILENAME:
        continue # skip non-image files and the logo file itself

    im = Image.open(filename)
    width, height = im.size


    # Add logo.
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Save changes.
    im.save(os.path.join(NEW_FOLDER_NAME, filename))

print("Done Adding Logo To All Images ... ^_^")
