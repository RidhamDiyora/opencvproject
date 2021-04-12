import cv2
import numpy as np

img = np.zeros((512,512,3))#uint8
#img[212:250] = 0,0,255
cv2.line(img,(0,0),(512,512),(255,0,0),2)
cv2.rectangle(img,(0,0),(212,212),(0,255,0),cv2.FILLED)
cv2.circle(img,(212,300),100,(0,0,255),cv2.FILLED)
cv2.putText(img,'Chashmish',(300,100),cv2.FONT_ITALIC,1,(0,255,255))

cv2.imshow('output',img)
cv2.waitKey(0)