import cv2 as cv
img= cv.imread('cat.jpg',1)
img1=cv.imread('cat.jpg',0)
cv.imshow('RGB image', img)
cv.imshow('Grey scale', img1)

cv.waitKey(0)
