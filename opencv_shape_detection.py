import cv2
import numpy as np

img = cv2.imread('C:/Users/Ridham Diyora/Pictures/Saved Pictures/shapes.jpg')
imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)



cv2.imshow('img',img)
cv2.imshow('imgGray',imgGray)
cv2.imshow('imgBlur',imgBlur)
cv2.waitKey(0)