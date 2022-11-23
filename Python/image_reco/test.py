import cv2
import numpy as np
import pandas as pd
img =cv2.imread('images/digits.png',cv2.IMREAD_GRAYSCALE)

cells=[np.hsplit(row,100) for row in np.vsplit(img,50)]
x= np.array(cells)
img_rows, img_cols =20,20
X= x.reshape(-1, img_rows, img_cols, 1)
y= pd.get_dummies(np.repeat(np.arange(10),500)).to_numpy()

from sklearn.model_selection import train_test_split
train_X, test_X, train_y, test_y= train_test_split(X,y, test_size=0.3, random_state=1)
