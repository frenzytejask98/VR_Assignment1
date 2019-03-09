import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

cv2.namedWindow("image", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
im = cv2.imread("1.jpeg")                        # Read image
imS = cv2.resize(im, (348, 464))                    # Resize image
cv2.imshow("image", imS)                            # Show image
cv2.waitKey(0)     
cv2.destroyAllWindows()

b = imS.copy()
# set green and red channels to 0
b[:, :, 1] = 0
b[:, :, 2] = 0


g = imS.copy()
# set blue and red channels to 0
g[:, :, 0] = 0
g[:, :, 2] = 0

r = imS.copy()
# set blue and green channels to 0
r[:, :, 0] = 0
r[:, :, 1] = 0


# RGB - Blue
brgb=cv2.imshow('B-RGB', b)
cv2.imwrite('brgb.jpeg', b)
# RGB - Green
grgb=cv2.imshow('G-RGB', g)
cv2.imwrite('grgb.jpeg',g)
# RGB - Red
rrgb=cv2.imshow('R-RGB', r)
cv2.imwrite('rrgb.jpeg', r)

b=cv2.imshow('Blue Channel', imS[:,:,0])
cv2.imwrite('b.jpeg', imS[:,:,0])
g=cv2.imshow('Green Channel', imS[:,:,1])
cv2.imwrite('g.jpeg', imS[:,:,1])
r=cv2.imshow('Red Channel', imS[:,:,2])
cv2.imwrite('r.jpeg', imS[:,:,2])

cv2.waitKey(0)
cv2.destroyAllWindows()