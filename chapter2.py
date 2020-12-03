import cv2
import numpy as np
img = cv2.imread('plastic1.jpg')
kernal = np.ones((5,5),np.uint8)
imgCanny =cv2.Canny(img,150,200)
imgDilation = cv2.dilate(imgCanny, kernal, iterations=1)
imgErotion = cv2.erode(imgDilation, kernal, iterations=1)
cv2.imshow('Image Dilation', imgDilation)
cv2.imshow('Image Erotion', imgErotion)
cv2.waitKey(0)