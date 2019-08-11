import cv2
import numpy as np


src_image_name = 'timg.jpg'
# img_rgb = cv2.imread(src_image_name)
#
# width, height = img_rgb.shape[:2]
# print(width, height)

from PIL import Image
im=Image.open(src_image_name)
width,height = im.size

im = im.convert("RGB")
r,g,b = im.getpixel((10,10))
data = im.getdata()
print(width,height)

image_arr = np.array(im)
print(image_arr)