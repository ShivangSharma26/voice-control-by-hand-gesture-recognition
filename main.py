import cv2
import time
import math
from hand_gesture import HandGesture
from volume_control import VolumeControl

cap = cv2.VideoCapture(0)
hand_gesture = HandGesture()
volume_control = VolumeControl()

while True:
    success, img = cap.read()
    img = hand_gesture.process(img)
    vol, volbar, volper = volume_control.update_volume(hand_gesture.length)
    # Update the UI elements with vol, volbar, volper...

    # Display the image
    cv2.imshow('Flip', img)
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break
