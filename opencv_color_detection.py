import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars',340,240)
cv2.createTrackbar('hue_min','TrackBars',0,179,empty)
cv2.createTrackbar('hue_max','TrackBars',179,179,empty)
cv2.createTrackbar('sat_min','TrackBars',0,255,empty)
cv2.createTrackbar('sat_max','TrackBars',255,255,empty)
cv2.createTrackbar('val_min','TrackBars',0,255,empty)
cv2.createTrackbar('val_max','TrackBars',255,255,empty)

while True:
    img = cv2.imread('C:/Users/Ridham Diyora/.vscode/python projects/pictures/ironman.jfif')
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos('hue_min','TrackBars')
    h_max = cv2.getTrackbarPos('hue_max','TrackBars')
    s_min = cv2.getTrackbarPos('sat_min','TrackBars') 
    s_max = cv2.getTrackbarPos('sat_max','TrackBars')
    v_min = cv2.getTrackbarPos('val_min','TrackBars')
    v_max = cv2.getTrackbarPos('val_max','TrackBars')

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow('output',img)
    cv2.imshow('hsv',imgHSV)
    cv2.imshow('Result',imgResult)
    cv2.waitKey(1)