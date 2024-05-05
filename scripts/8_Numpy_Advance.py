import cv2
import numpy as np

# Define the dimensions of the image
width = 640
height = 480

# Create a blank image
nature_image = np.zeros((height, width, 3), dtype=np.uint8)

# Fill the sky region with blue color
nature_image[:, :] = [135, 206, 235]  # RGB values for sky blue

# Draw a sun (circle) in the center of the image
cv2.circle(nature_image, (width // 2, height // 2), 100, (0, 255, 255), -1)  # Yellow color for sun

# Fill the bottom region with green color for grass
nature_image[height // 2:, :] = [0, 128, 0]  # RGB values for green

# Display the nature image using OpenCV
cv2.imshow('Nature Image Zeros', nature_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
