import cv2

cap = cv2.VideoCapture('C:/Users/Ridham Diyora/.vscode/python projects/pictures/panda video.webm')

while True:
    success , img = cap.read()
    cv2.imshow('video', img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
