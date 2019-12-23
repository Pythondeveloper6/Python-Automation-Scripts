"__mahmoud_ahmed__"

import os
img_types = ['jpg' , 'png' , 'jpeg']
for root, dirs, files in os.walk('.'):
    for i,f in enumerate(files):
        absname = os.path.join(root, f)
        img_type = absname.split('.')[2]

        if img_type in img_types :
            newname = '{}.{}'.format(str(i),img_type)
            os.rename(f, newname)
