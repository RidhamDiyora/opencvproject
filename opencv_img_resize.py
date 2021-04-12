import cv2

img = cv2.imread('C:/Users/Ridham Diyora/.vscode/python projects/pictures/ironman.jfif')

imgResize = cv2.resize(img,(480,640))
imgCropped = img[0:100,0:200]

cv2.imshow('img',img)
cv2.imshow('Resize',imgResize)
cv2.imshow('cropped',imgCropped)
cv2.waitKey(0)  
