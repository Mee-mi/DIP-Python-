import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img= cv.imread('cat.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('cat grey',img)
cv.waitKey(0)
