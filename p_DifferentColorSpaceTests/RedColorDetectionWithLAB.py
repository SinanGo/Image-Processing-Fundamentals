# This is another color space named LAB
# You can change the parameters and observe the differences.

import cv2
import numpy as np

image = cv2.imread("v2TestImage2.jpg")
# Also try v2TestImage.jpg

# Red color ranges for LAB Color space
LABLower1 = np.array([0, 145, 153])
LABUpper1 = np.array([255, 255, 255])

LABLower2 = np.array([0,149,118])
LABUpper2 = np.array([255,255,255])

LABImage = cv2.cvtColor(image,cv2.COLOR_BGR2LAB)

LABMask1 = cv2.inRange(LABImage,LABLower1,LABUpper1)
LABMask2 = cv2.inRange(LABImage,LABLower2,LABUpper2)

LABFullMask = LABMask1 + LABMask2

result = cv2.bitwise_and(image,image,mask=LABFullMask)

cv2.imshow("Original Image",image)
cv2.imshow("LAB Image",LABImage)
cv2.imshow("LAB Mask1", LABMask1)
cv2.imshow("LAB Mask2", LABMask2)
cv2.imshow("LAB Full Mask", LABFullMask)
cv2.imshow("LAB Result",result)

cv2.waitKey(0)
cv2.destroyAllWindows()