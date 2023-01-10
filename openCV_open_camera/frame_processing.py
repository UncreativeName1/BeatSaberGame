import cv2
import matplotlib.pyplot as plt
import numpy as np

def get_brightest_point(img_main):
    img_rgb = np.copy(img_main)

    # convert the image to grey scale
    img_grey = np.copy(img_main)
    img_grey = cv2.cvtColor(img_grey, cv2.COLOR_BGR2GRAY)

    # apply median blur
    median_blur = cv2.medianBlur(img_grey, 21) 

    # plt.subplot(1, 1, 1)  
    # plt.imshow(median_blur, cmap="gray")  
    # plt.show()  

    # find the max brightness x and y values
    max_x = cv2.minMaxLoc(median_blur)[3][0]
    max_y = cv2.minMaxLoc(median_blur)[3][1]

    print("x: " + str(max_x) + ",  y: " + str(max_y))

    # make a square of length 50 to display the brightest spot
    s = 50
    coordinate_left = (max_x - s, max_y - s)
    coordinate_right = (max_x + s, max_y + s)
    color = (255, 0, 0)
    t = 5

    brightest_box =np.copy(img_rgb)
    brightest_box = cv2.rectangle(brightest_box, coordinate_left, coordinate_right, color, t)

    cv2.circle(img_main, (max_x, max_y), 7, (125, 125, 125), -1)
    # show the plot
    # plt.subplot(1, 1, 1)  
    # plt.imshow(brightest_box, cmap="gray")  
    # plt.show()  
