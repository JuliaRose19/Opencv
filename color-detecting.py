import cv2
import numpy as np
path = 'plasticbag2.jpeg'
def empty(a):
    pass

cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars',640,240)
cv2.createTrackbar('Hue Min','TrackBars',0,179,empty)
cv2.createTrackbar('Hue Max','TrackBars',175,179,empty)
cv2.createTrackbar('Sat Min','TrackBars',0,255,empty)
cv2.createTrackbar('Sat Max','TrackBars',212,255,empty)
cv2.createTrackbar('Value Min','TrackBars',14,255,empty)
cv2.createTrackbar('Value Max','TrackBars',142,255,empty)
while True:
    img = cv2.imread(path)
    imgResize = cv2.resize(img,(640,480))
    imgHSV= cv2.cvtColor(imgResize , cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('Hue Min','TrackBars')
    h_max = cv2.getTrackbarPos('Hue Max', 'TrackBars')
    s_min = cv2.getTrackbarPos('Sat Min', 'TrackBars')
    s_max = cv2.getTrackbarPos('Sat Max', 'TrackBars')
    v_min = cv2.getTrackbarPos('Value Min', 'TrackBars')
    v_max = cv2.getTrackbarPos('Value Max', 'TrackBars')
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(imgResize,imgResize,mask=mask)

    cv2.imshow('HSV',imgHSV)
    cv2.imshow('Mask',mask)
    cv2.imshow('Result', imgResult )
    cv2.waitKey(1)