import cv2 as cv
img= cv.imread('cat.jpg')
print(img.shape)
print("total number of pixel", img.size)
cv.imshow('output', img)
img.save('cat pix.jpg')
cv.waitKey(0)