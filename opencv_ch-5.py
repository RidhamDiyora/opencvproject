import cv2
import numpy as np

width,height = 259,194
img = cv2.imread('C:/Users/Ridham Diyora/.vscode/python projects/pictures/cards.png')
pts1 = np.float32([[181,41],[253,76],[204,179],[134,144]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow('output',imgOutput)
cv2.waitKey(0)