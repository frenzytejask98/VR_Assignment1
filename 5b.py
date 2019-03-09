import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
imge = cv2.imread('1.jpeg',0)
imS = cv2.resize(imge, (348, 464))  
cv2.imwrite('grey.jpeg',imS)
equ = cv2.equalizeHist(imS)
res = np.hstack((imS,equ)) #stacking images side-by-side
cv2.imwrite('res.jpeg',res)
cv2.imshow('gra',res)
cv2.waitKey(0)
cv2.destroyAllWindows()