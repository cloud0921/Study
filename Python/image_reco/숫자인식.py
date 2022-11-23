import cv2
import numpy as np
cap =cv2.VideoCapture(0)
if cap.isOpened():
    while True:
        ret,img=cap.read()
        if ret:
            g_img = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2GRAY)
            
    