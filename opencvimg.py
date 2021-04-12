import cv2
import numpy as np

img = cv2.imread('C:/Users/Ridham Diyora/.vscode/python projects/pictures/ironman.jfif')
kernel = np.ones((5,5),np.uint8)
imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(5,5),0)
imgcanny = cv2.Canny(img , 100,100)
imgDialation = cv2.dilate(imgGray,kernel,iterations=1)
imgEroded = cv2.erode(imgGray,kernel,iterations=1)
cv2.imshow('Gray',imgGray)
cv2.imshow('Blur',imgBlur)
cv2.imshow('canny',imgcanny)
cv2.imshow('Dialation',imgDialation)
cv2.imshow('Eroded',imgEroded)
cv2.waitKey(0)