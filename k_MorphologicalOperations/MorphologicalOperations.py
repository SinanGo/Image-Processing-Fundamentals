import cv2
import numpy as np

image = cv2.imread("NoisyPicture2.jpg")

kernel = np.ones((3,3),np.uint8)
#kernel = np.ones((5,5),np.uint8) # try with this one. See the difference

erosion = cv2.erode(image,kernel,iterations = 1)
dilation = cv2.dilate(image,kernel,iterations = 1)
dilation2 = cv2.dilate(erosion,kernel,iterations = 1)

opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel) #erosion+dilation
closing = cv2.morphologyEx(image,cv2.MORPH_CLOSE, kernel) #dilation+erosion

gradian = cv2.morphologyEx(image,cv2.MORPH_GRADIENT,kernel) #dilation-erosion
topHat = cv2.morphologyEx(image,cv2.MORPH_TOPHAT,kernel) #original-opening
blackHat = cv2.morphologyEx(image,cv2.MORPH_BLACKHAT,kernel) #closing-original


cv2.imshow("Original", image)
cv2.imshow("Erosion",erosion)
cv2.imshow("Dilation",dilation) 
cv2.imshow("Erosion+Dilation",dilation2)
cv2.imshow("Opening",opening)
cv2.imshow("Closing",closing)
cv2.imshow("Gradian",gradian)
cv2.imshow("TopHat",topHat)
cv2.imshow("Black Hat",blackHat)

cv2.waitKey(0)
cv2.destroyAllWindows()
