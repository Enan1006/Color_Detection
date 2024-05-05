import cv2 as cv
import numpy as np


def get_color(color):
    c = np.uint8([[color]])
    convert_hsv = cv.cvtColor(c, cv.COLOR_BGR2HSV)
    get_hue = convert_hsv[0][0][0]

    # wrap around
    lower_limit_hue = (get_hue - 10) % 180
    higher_limit_hue = (get_hue + 10) % 180

    lower_limit = np.array([lower_limit_hue, 0, 0], dtype=np.uint8)
    upper_limit = np.array([higher_limit_hue, 30, 30], dtype=np.uint8)

    return lower_limit, upper_limit
