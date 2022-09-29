import cv2 as cv
from PIL import Image
img= Image.open('cat.jpg')
img.thumbnail((300,300))
img.show()
img.save('cat resol.jpg')