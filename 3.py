import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

im = cv2.imread("1.jpeg")                        # Read image
imS = cv2.resize(im, (348, 464)) 
labimg = cv2.cvtColor(imS,cv2.COLOR_BGR2Lab)
cv2.imshow('L*A*B*',labimg)
cv2.imwrite('lab.jpeg',labimg)
cv2.waitKey(0)
cv2.destroyAllWindows()