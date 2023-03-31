# Open a red circle image from your phone or etc. 
# and observe the changes

import cv2
import numpy as np

cam = cv2.VideoCapture(0)

# red color ranges in LAB color space
lower1 = np.array([0,154,163])
upper1 = np.array([255,255,255])
lower2 = np.array([0,174,143])
upper2 = np.array([255,255,255])

while True:

    ret, image = cam.read()

    imageLAB = cv2.cvtColor(image,cv2.COLOR_BGR2LAB) # convert the format of the image to lab
    
    imageLABMask1 = cv2.inRange(imageLAB,lower1,upper1)
    imageLABMask2 = cv2.inRange(imageLAB,lower2,upper2)
    imageLABMaskTotal = imageLABMask1 + imageLABMask2

    # Search for HoughCircles method in openCV Python
    # or look at the documentation

    # it returns a numpy array of circles. It may catch more than one circle in an image.
    # however, this algorithm uses the first one -> circles[0]
    circles = cv2.HoughCircles(imageLABMaskTotal,cv2.HOUGH_GRADIENT, dp = 2,                 
                        minDist=50,param1 = 100, param2 = 50, minRadius=20,maxRadius=100)      

    # if you can not catch a circle, you can lower param2 or change other parameters.

    if circles is not None:

        # Draw the detected circle for just looking up
        
        circles = np.round(circles[0, :]).astype("int") # Turn parameters to integers

        circleCenter=(circles[0, 0], circles[0, 1]) # Assign the parameters of circles[0]
        circleRadius=circles[0, 2]                  # to varibales for readability

        cv2.circle(image, circleCenter,circleRadius, color=(255, 0, 0), thickness=2)
        
    if cv2.waitKey(100) & 0x0FF == ord("q"): # FPS is 10. Is it enough for real usage?
        break

    # you may have better understanding if you show different red objects to the camera
    cv2.imshow("Mask2",imageLABMask2)
    cv2.imshow("Mask1",imageLABMask1)
    cv2.imshow("Total Mask", imageLABMaskTotal)
    cv2.imshow("Cam", image)

cam.release()
cv2.destroyAllWindows()

    
