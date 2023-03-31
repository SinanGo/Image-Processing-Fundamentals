# It can be easier to use different color spaces instead of RGB
# There is no one true color space and one true color range
# It depends on what kind of task you want do achieve
# You can change the range parameters and observe the changes.

import cv2
import numpy as np

image = cv2.imread("v2TestImage.jpg")
# Also try v2TestImage2.jpg

# Red color ranges for HSV Color space
HSVLower1 = np.array([0, 100, 20])
HSVUpper1 = np.array([10, 255, 255])

HSVLower2 = np.array([120,60,20])
HSVUpper2 = np.array([179,255,255])

HSVImage = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

# we create two masks and combine them to have a better red color catch.
# So, we could use just one of them. 
# You will understand better when you observe HSVMask1, HSVMask2 and HSVFullMask

HSVMask1 = cv2.inRange(HSVImage,HSVLower1,HSVUpper1)
HSVMask2 = cv2.inRange(HSVImage,HSVLower2,HSVUpper2)

HSVFullMask = HSVMask1 + HSVMask2

result = cv2.bitwise_and(image,image,mask=HSVFullMask)

cv2.imshow("Original Image",image)
cv2.imshow("HSV Image",HSVImage)
cv2.imshow("HSV Mask1", HSVMask1)
cv2.imshow("HSV Mask2", HSVMask2)
cv2.imshow("HSV Full Mask", HSVFullMask)
cv2.imshow("HSV Result",result)

cv2.waitKey(0)
cv2.destroyAllWindows()