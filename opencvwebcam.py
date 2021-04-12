import cv2

cap = cv2.VideoCapture(0)
cap.set(3,480)
cap.set(4,480)

while True:
    success , img = cap.read()
    cv2.imshow('webcam',img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break