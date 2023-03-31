import cv2
import numpy as np

# create an image with the spesified shape and datatype
# All pixels are three times 0! ---> (0,0,0) : Black color
pic = np.zeros((150,150,3),dtype="uint8")

cv2.imshow("zeros",pic)
print(pic)

cv2.waitKey(0)
cv2.destroyAllWindows()