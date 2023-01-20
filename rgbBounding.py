import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to rgb
    rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    #hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([0,0,150])
    upper_blue = np.array([100,100,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(rgb, lower_blue, upper_blue)
    contours,hierarchy = cv.findContours(mask, 1, 2)
    if len(contours) == 1:
        area = cv.contourArea(contours[0])
        x,y,w,h = cv.boundingRect(contours[0])
        cv.rectangle(mask,(x,y),(x+w,y+h),color=(255,255,255),thickness=2)
    elif len(contours) > 1:
        for i in contours:
            area = cv.contourArea(i)
            x,y,w,h = cv.boundingRect(i)
            cv.rectangle(mask,(x,y),(x+w,y+h),color=(255,255,255),thickness=2)
    else:
        #no contour found
        pass
    
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()