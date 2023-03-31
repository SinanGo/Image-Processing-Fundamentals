import cv2

pic = cv2.imread("ImageToManipulate2.jpg")

# usage : source, top, bottom, left, right, mode
reflectedImage = cv2.copyMakeBorder(pic,100,100,50,50,cv2.BORDER_REFLECT)
extendedImage = cv2.copyMakeBorder(pic,50,50,25,25,cv2.BORDER_REPLICATE)
repeatedImage = cv2.copyMakeBorder(pic,0,0,pic.shape[1],pic.shape[1],cv2.BORDER_WRAP)
BorderedImage = cv2.copyMakeBorder(pic,5,5,5,5,cv2.BORDER_CONSTANT,
                                    value=(255,100,25))

# run the code and observe the changes
cv2.imshow("Reflected Image", reflectedImage)
cv2.imshow("Extended Image", extendedImage)
cv2.imshow("Repeated Image", repeatedImage)
cv2.imshow("Bordered Image", BorderedImage)

cv2.waitKey(0)
cv2.destroyAllWindows()