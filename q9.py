#!/usr/bin/env python
# coding: utf-8

# In[73]:


import cv2
import numpy as np
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import pandas as pd


# In[74]:


def single_ch_hist(image, channels, bins, chrange, color):
    hist = cv2.calcHist(image, channels, None, bins, chrange)
    return hist

def plot_hist(image):
    histarr = []
    histarr.append(single_ch_hist(image, [0], [32], [0, 179], 'r'))
    histarr.append(single_ch_hist(image, [1], [32], [0, 255], 'g'))
    histarr.append(single_ch_hist(image, [2], [32], [0, 255], 'y'))
    histarr = np.asarray(histarr)
    histarr = histarr.reshape((3, 32))
    plt.show()
    return histarr


# In[116]:


folderarr = ["landscape","night","portrait"]
finarr = []
for i in folderarr:
    for j in range(1,44):
        image = cv2.imread(i + "/" + str(j) + ".jpg");
        print(i + "/" + str(j) + ".jpg")
        image_new = cv2.resize(image, (600, 600));
        immm = cv2.cvtColor(image_new, cv2.COLOR_BGR2HSV)
        arr = plot_hist(immm)
        arrr = plot_hist(image_new)
        finarr.append(arr)
        finarr.append(arrr)
z = np.asarray(finarr)
z = z.reshape(129, 192)
data = pd.DataFrame(z)
data.columns = [str(col) + '_col' for col in data.columns]


# In[107]:


folderarr = ["landscape","night","portrait"]
labels = []
for i in folderarr:
    for j in range(43):
        labels.append((i))


# In[108]:


label = pd.DataFrame(labels, columns=["labels"])
datacon = pd.concat([data, label], axis = 1)


# In[109]:


from sklearn.utils import shuffle
datacon = shuffle(datacon)


# In[124]:


X=datacon.drop(columns='labels')    
y=datacon['labels']


# In[125]:


scores=[]
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(algorithm='auto', metric_params=None, n_jobs=None, n_neighbors=3,weights='uniform')
cv_score = np.mean(cross_val_score(knn, X, y, cv=6))
scores.append(cv_score)
print(scores)

