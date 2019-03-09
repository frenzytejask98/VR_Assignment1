import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from skimage.util import random_noise
def noisy(image):
    row,col,ch = image.shape
    s_vs_p = 0.5
    amount = 0.05
    out = np.copy(image)
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
          for i in image.shape]
    out[coords] = 1

    # Pepper mode
    num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
          for i in image.shape]
    out[coords] = 0
    return out
imgg=cv2.imread('6.png')

noise=noisy(imgg)
cv2.imwrite('noise.png',noise)
med = cv2.medianBlur(imgg,5)
cv2.imshow('Noise',noise)
cv2.imshow('Filter',med)
cv2.imwrite('filter.png',med)
cv2.waitKey(0)
cv2.destroyAllWindows()