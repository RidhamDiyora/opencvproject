import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)

with open ('myDataList.text') as f:
    myDatalist = f.read().splitlines()
print(myDatalist)

while True:
    success, img = cap.read()

    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        #print(myData)

        if myData in myDatalist:
            myOutput = 'Authorized'
            myColor = (0,255,0)
        else:
            print('Un-Authorized')
            myOutput = 'Un-Authorized'
            myColor = (0,0,255)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        pts2 = barcode.rect
        cv2.polylines(img,[pts],True,myColor,3) 
        cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_COMPLEX,1,myColor,1)

    cv2.imshow('webcam',img)
    cv2.waitKey(1)