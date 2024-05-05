# 1. Kernel Blur
# 2. Box Filtering
# 3. Blur() function
# 4. Gaussian Blur
# 5. Median Blur
# 6. Bilateral Filtering
# 7. Sharpening Image
import cv2 as cv
import numpy as np

# All the functions are uses for image pre-processing
img = cv.imread('../resources/door-1.jpg')
# Kernel blurring using filter2D()
kernel_25 = np.ones((5, 5), np.float32) / 25.0
output_kernel = cv.filter2D(img, -1, kernel_25)
# creating a kernel with specific number of rows and columns then divide it by the multiplication
# of num of rows and num of columns is called Normalizing

# Box filter and Blur function blurring
box_filter_img = cv.boxFilter(img, -1, (5, 5), normalize=False)
blur_img = cv.blur(img, (5, 5))

# Gaussian Blur
gauss_blur = cv.GaussianBlur(img, (5, 5), 0)

# Bilateral filter
bilateral_filter = cv.bilateralFilter(img, 5, 6, 0)

# Add weight for sharpening images
sharpen_1 = cv.addWeighted(img, 2.5, gauss_blur, 1.5, 0)
sharpen_2 = cv.addWeighted(img, 5.5, gauss_blur, 4.5, 0)
sharpen_3 = cv.addWeighted(img, 8.5, gauss_blur, 7.5, 0)

cv.imshow('Original Image', img)
cv.imshow('Kernel Image', output_kernel)
cv.imshow('Box Filter Image', box_filter_img)
cv.imshow('Blur Image', blur_img)
cv.imshow('Gaussian Blur', gauss_blur)
cv.imshow('Bilateral Filter', bilateral_filter)
cv.imshow('Sharpe Image 1', sharpen_1)
cv.imshow('Sharpe Image 2', sharpen_2)
cv.imshow('Sharpe Image 3', sharpen_3)

cv.waitKey(0)
cv.destroyAllWindows()
