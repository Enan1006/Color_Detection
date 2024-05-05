import cv2 as cv
import numpy as np

img = cv.imread('../resources/iloveimg-resized/beautiful-sunset.jpg')
img_resized = cv.resize(img, (640,360))
img_grey = cv.cvtColor(img_resized, cv.COLOR_BGR2GRAY)

gedient_sobel_x = cv.Sobel(img_grey, -1, 1, 0)
gedient_sobel_y = cv.Sobel(img_grey, -1, 0, 1)

cv.imshow('Original img', img_resized)
cv.imshow('Sobel X img', gedient_sobel_x)
cv.imshow('Sobel Y img', gedient_sobel_y)

cv.waitKey(0)
cv.destroyAllWindows()