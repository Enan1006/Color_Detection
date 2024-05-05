import cv2
import numpy as np

# Define the dimensions of the image
width = 640
height = 480

# Create a blank image with np.zeros
nature_image_zeros = np.zeros((height, width, 3), dtype=np.uint8)

# Fill the sky region with blue color
nature_image_zeros[:height // 2, :] = [135, 206, 235]  # RGB values for sky blue

# Fill the bottom region with green color for grass
nature_image_zeros[height // 2:, :] = [0, 128, 0]  # RGB values for green

# Create a blank image with np.ones
nature_image_ones = np.ones((height, width, 3), dtype=np.uint8) * 255

# Fill the sky region with light blue color
nature_image_ones[:height // 2, :] = [173, 216, 230]  # RGB values for light blue

# Fill the bottom region with light green color for grass
nature_image_ones[height // 2:, :] = [144, 238, 144]  # RGB values for light green

# Display the nature images using OpenCV
cv2.imshow('Nature Image with np.zeros', nature_image_zeros)
cv2.imshow('Nature Image with np.ones', nature_image_ones)
cv2.waitKey(0)
cv2.destroyAllWindows()
