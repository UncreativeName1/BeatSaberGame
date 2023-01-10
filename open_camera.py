import cv2
import matplotlib.pyplot as plt
import numpy as np

from frame_processing import get_brightest_point

# create video capturing
vid = cv2.VideoCapture(0)

if not vid.isOpened():
    print("Cannot open camera")
    exit()

while (True):
    # Get current frame
    ret, frame = vid.read()
    if not ret:
        print("Stopped receiving stream. Exiting ...")
        break

    # Call image processing function
    result = get_brightest_point(frame)

    # Display the resulting frame
    cv2.imshow('frame', frame)


    # press q to exit the video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the video
vid.release()
cv2.destroyAllWindows()
