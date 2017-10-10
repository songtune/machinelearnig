import os
import glob
from PIL import Image

files = glob.glob('/Users/matsumurayuu/Desktop/test.jpg')

for f in files:
    img = Image.open(f)
    img_resize = img.resize((int(50), int(50)))
    ftitle, fext = os.path.splitext(f)
    img_resize.save(ftitle + '_half' + fext)