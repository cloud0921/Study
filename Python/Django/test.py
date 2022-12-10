import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("house.jpg", cv2.IMREAD_GRAYSCALE)

kernel = np.array([[0,0,0],[0,1,-1],[0,0,0]])
output = cv2.filter2D(img,-1,kernel)

cv2.imshow("House",img)
cv2.imshow("filter2D",output)
cv2.waitKey()
cv2.destroyAllWindows()