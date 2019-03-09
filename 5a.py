import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
imggg = cv2.imread('1.jpeg',0)
imS = cv2.resize(imggg, (348, 464))  
def whitening(img):
    mean = np.mean(img)
    sd = np.std(img)
    temp = np.copy(img)
    temp = (img - mean) / sd

    min = np.min(temp)
    max = np.max(temp)
    temp = (temp - mn) / (mx - mn)
    return temp
whit = whitening(imS)
cv2.imshow("before",imS)
cv2.imwrite('begore.jpeg',imS)
cv2.imshow("white",whit)
cv2.imwrite('white.jpeg',whit)

cv2.waitKey(0)
cv2.destroyAllWindows()