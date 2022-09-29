import cv2 as cv
from PIL import Image
img= Image.open('cat.jpg')
img.rotate(45).show()
img.save('cat rotate.jpg')