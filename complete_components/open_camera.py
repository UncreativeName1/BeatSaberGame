import cv2
import numpy as np
from detect_light import *

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "Coord: ({self.x}, {self.y})"


# remove the first n elements from arr
def remove_front(arr, n):
    arr_len = len(arr)
    if arr_len < n:
        return []
    while n > 0:
        arr.pop(0)
        n -= 1
    return arr

color = (0, 255, 0)
thickness = 9
# the number of recent frames to keep the movement line on for
frames_tracked = 10
cur_len = 0

# create video capturing
vid = cv2.VideoCapture(0)
# array of Coords across multiple frames
coords = []

if not vid.isOpened():
    print("Cannot open camera")
    exit()

# press q to exit the video
while (cv2.waitKey(1) & 0xFF != ord('q')):
    # Get current frame
    ret, frame = vid.read()
    if not ret:
        print("Stopped receiving stream. Exiting ...")
        break

    # call image processing function
    brightest_point = get_brightest_point(frame)
    x = brightest_point['center_x']
    y = brightest_point['center_y']
    c = Coord(x, y)

    coords.append(c)
    cur_len += 1

    frames_exceeded = cur_len - frames_tracked

    if cur_len > frames_tracked:
        remove_front(coords, frames_exceeded)
        cur_len -= frames_exceeded

    print(c)

    for i in range (1, cur_len):
        prev_x = coords[i].x
        prev_y = coords[i].y
        cur_x = coords[i-1].x
        cur_y = coords[i-1].y
        # print(prev_x, prev_y, cur_x, cur_y)

        prev_point = (prev_x, prev_y)
        cur_point = (cur_x, cur_y)
        cv2.line(frame, prev_point, cur_point, color, thickness)

    # Display the resulting frame
    cv2.imshow('frame', frame)


# release the video
vid.release()
cv2.destroyAllWindows()
