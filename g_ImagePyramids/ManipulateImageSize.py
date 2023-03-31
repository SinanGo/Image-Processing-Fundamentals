import cv2

pic = cv2.imread("ImageToManipulate.jpg")

DoublePic = cv2.pyrUp(pic) 
HalfPic = cv2.pyrDown(pic)

cv2.imshow("Pic",pic)
cv2.imshow("Double Pic", DoublePic)
cv2.imshow("Half Pic", HalfPic)

# run the program and observe the values
print("Pic Shape: ",pic.shape)
print("Double Pic Shape: ",DoublePic.shape)
print("Half Pic Shape", HalfPic.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()