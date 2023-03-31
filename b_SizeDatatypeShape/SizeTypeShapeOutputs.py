import cv2

picture = cv2.imread("aldebaran22v1.jpg") # have 3 channels : blue,green,red
picture2 = cv2.imread("aldebaran22v2.jpg",0) # have only one channel

cv2.imshow("Aldebaran-1",picture)
cv2.imshow("Aldebaran-2",picture2)

print("Picture-1 Shape :",picture.shape) # return the dimensions and # of channels as a tuple of integers
print("Picture-1 Size :",picture.size) # multiply above 
print("Picture-1 Data Type :",picture.dtype) # return the datatype of the image

print("Picture-2 Shape :",picture2.shape) # height,width,channel count
print("Picture-2 Size :",picture2.size) # height*width*channelCount
print("Picture-2 Data Type :",picture2.dtype) # uint8 : unsigned 8-bit int (0,255)

cv2.waitKey(0)
cv2.destroyAllWindows()