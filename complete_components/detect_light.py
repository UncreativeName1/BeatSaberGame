import cv2

pi = 3.1415926535897932384626

def circularity(area, perimeter):
    return (4 * pi * area) / (perimeter ** 2)

# creates terminal arguments
#arg_par = argparse.ArgumentParser()
#arg_par.add_argument("-i", "--image", required=True, help="path to img file")
#args = vars(arg_par.parse_args())

def get_brightest_point(img):
    # grayscale and blur image
    grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.medianBlur(grayscaled, 21)

    min_max_info = cv2.minMaxLoc(blurred)
    brightest_value = min_max_info[1]

    print(brightest_value)

    # any pixel >= 200 is set to white (255) and any < 200 are set to black
    brightest_only = cv2.threshold(blurred, brightest_value-3, 255, cv2.THRESH_BINARY)[1]

    # remove small areas/noise
    brightest_only = cv2.erode(brightest_only, None, iterations=2)
    brightest_only = cv2.dilate(brightest_only, None, iterations=4)

    # find contours
    contours, hierarchy = cv2.findContours(brightest_only, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    num_contours = len(contours)
    #
    #initialize to smallest possible
    max_circ = 0
    most_circ_contour = None

    # find contour with max circularity
    for i, contour in enumerate(contours):
        print("current: contour {} of {}".format(i+1, num_contours))
        area = cv2.contourArea(contour)
        perim = cv2.arcLength(contour, True)
        circ = circularity(area, perim)
        if circ > max_circ or i == 0:
            most_circ_contour = contour
            max_circ = circ

    # centroid of the most circular moment
    img_moment = cv2.moments(most_circ_contour)
    #print(img_moment)
    if img_moment["m00"] != 0:
        centerX = int(img_moment["m10"]/img_moment["m00"])
        centerY = int(img_moment["m01"]/img_moment["m00"])
    else:
        centerX, centerY = 0,0
        print("ERROR")
    brightest_point_info = {
        "center_x": centerX,
        "center_y": centerY
    }
    return brightest_point_info

def print_brightest_point(img):
    brightest_point = get_brightest_point(img)
    centerX = brightest_point['center_x']
    centerY = brightest_point['center_y']

    #cv2.drawContours(img, [most_circ_contour], -1, (0, 255, 0), 2)
    cv2.circle(img, (centerX, centerY), 7, (125, 125, 125), -1)
    print("x: {}, y: {}".format(centerX, centerY))
    #cv2.putText(img, "center", (centerX - 20, centerY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
