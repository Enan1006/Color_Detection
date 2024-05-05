import bbox
import cv2 as cv
import numpy as np
from Util import get_color
from PIL import Image

cap = cv.VideoCapture(0)
black = [0, 0, 0]
while True:
    ret, frame = cap.read()
    grayed = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_limit, upper_limit = get_color(color=black)
    mask = cv.inRange(grayed, lower_limit, upper_limit)
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    cv.imshow('Frame', grayed)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()