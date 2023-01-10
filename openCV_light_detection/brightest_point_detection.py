from pathlib import Path
import cv2 
import matplotlib.pyplot as plt
import numpy as np

# read in the images
img_src = str(Path(__file__).parent) + "/images/1.jpg"
img_main = cv2.imread(img_src)
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

# make a square of length 50 to display the brightest spot
s = 50
coordinate_left = (max_x - s, max_y - s)
coordinate_right = (max_x + s, max_y + s)
color = (255, 0, 0)
t = 5

brightest_box =np.copy(img_rgb)
brightest_box = cv2.rectangle(brightest_box, coordinate_left, coordinate_right, color, t)

# show the plot
plt.subplot(1, 1, 1)  
plt.imshow(brightest_box, cmap="gray")  
plt.show()  

# save the image to the file
# cv2.imwrite("/Users/petemango/SIDE PROJECTS/beatSaberProject/openCV_light_detection/processed_images/stock_image.jpg", brightest_box)
