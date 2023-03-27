from wincap import Screencap
import numpy as np
import cv2 as cv

k = Screencap.take_screenshot()
k = np.array(k)

k = k[214:657, 1157:1594]

cv.imshow('test', k)
cv.waitKey(0)

cv.destroyAllWindows()