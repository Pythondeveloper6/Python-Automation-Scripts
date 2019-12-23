

import os
from PIL import Image

#SQUARE_FIT_SIZE = 300
SQUARE_FIT_SIZE = int(input(" Enter Size : "))
NEW_FOLDER_NAME = input("Enter The New Folder Name : ")



os.makedirs(NEW_FOLDER_NAME, exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')):
        continue # skip non-image files and the logo file itself

    im = Image.open(filename)
    width, height = im.size

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image.
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))



    # Save changes.
    im.save(os.path.join(NEW_FOLDER_NAME, filename))

print('Done Resizing All Images ... ^_^')
