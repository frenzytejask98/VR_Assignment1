import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

im = cv2.imread("1.jpeg")                        # Read image
imS = cv2.resize(im, (348, 464)) grayscale = cv2.cvtColor(imS, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',grayscale)
cv2.imwrite('grayscale.jpeg',grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()