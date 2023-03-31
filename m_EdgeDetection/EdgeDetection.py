import cv2
import numpy as np

image = cv2.imread("RedTarget.jpg")

grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# change parameters and see the difference

blurredImage = cv2.GaussianBlur(image,(5,5),0)
blurredGrayImage = cv2.GaussianBlur(grayImage,(3,3),0) 

EdgeDetectedImage = cv2.Canny(blurredImage,50,150)        
EdgeDetectedGrayImage = cv2.Canny(blurredGrayImage,50,150)

cv2.imshow("Images", np.hstack([blurredImage,cv2.cvtColor(blurredGrayImage,cv2.COLOR_GRAY2BGR)]))
cv2.imshow("Edges", np.hstack([EdgeDetectedImage,EdgeDetectedGrayImage]))

cv2.waitKey(0)
cv2.destroyAllWindows()

