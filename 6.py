import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

imge = cv2.imread('1.jpeg')
imS = cv2.resize(imge, (348, 464)) 
gaus = cv2.GaussianBlur(imS,(1,1),cv2.BORDER_DEFAULT)
cv2.imwrite('gau11.jpeg',gaus)
gau = cv2.GaussianBlur(imS,(3,1),cv2.BORDER_DEFAULT)
cv2.imwrite('gau21.jpeg',gau)
ga = cv2.GaussianBlur(imS,(5,1),cv2.BORDER_DEFAULT)
cv2.imwrite('gau31.jpeg',ga)
g = cv2.GaussianBlur(imS,(7,1),cv2.BORDER_DEFAULT)
cv2.imwrite('gau41.jpeg',g)
res = np.hstack((imS,gaus, gau, ga,g))
cv2.imwrite('stack1.jpeg',res)
gauss = cv2.GaussianBlur(imS,(1,3),cv2.BORDER_DEFAULT)
cv2.imwrite('gau12.jpeg',gauss)
gaussi = cv2.GaussianBlur(imS,(1,5),cv2.BORDER_DEFAULT)
cv2.imwrite('gau13.jpeg',gaussi)
gaussia = cv2.GaussianBlur(imS,(1,7),cv2.BORDER_DEFAULT)
cv2.imwrite('gau14.jpeg',gaussia)
reso = np.hstack((imS,gaus, gauss, gaussi,gaussia))
cv2.imwrite('stack2.jpeg',reso)
cv2.imshow('Blur',gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()