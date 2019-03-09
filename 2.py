import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

im = cv2.imread("1.jpeg")                        # Read image
imS = cv2.resize(im, (348, 464)) 
hsvimg = cv2.cvtColor(imS, cv2.COLOR_BGR2HSV)#HSV

h, s, v = cv2.split(hsvimg)
s.fill(255)
v.fill(255)
hsv_img = cv2.merge([h, s, v])

out = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
s=cv2.imshow('Saturation Channel', out[:,:,1])
cv2.imwrite('s.jpeg', out[:,:,1])
v=cv2.imshow('V Channel', out[:,:,2])
cv2.imwrite('v.jpeg', out[:,:,2])

cv2.imshow('H', out)
cv2.imwrite('hsv.jpeg',hsvimg)
cv2.imwrite('h.jpeg', out)

cv2.waitKey(0)
cv2.destroyAllWindows()