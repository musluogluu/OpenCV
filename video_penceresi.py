import cv2
from time import time

vid = cv2.VideoCapture(0)
while True:
    ret, frame = vid.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    print("Program Active")

vid.release()
cv2.destroyAllWindows()