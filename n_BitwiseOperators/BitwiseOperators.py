import cv2
import numpy as np

pic1 = cv2.imread("BitwiseOperations1.jpg")
pic2 = cv2.imread("BitwiseOperations2.jpg")

# black : 0 , white : 1

AndOp = cv2.bitwise_and(pic1,pic2)
OrOp = cv2.bitwise_or(pic1,pic2)
XorOp = cv2.bitwise_xor(pic1,pic2)
NotOp = cv2.bitwise_not(pic1)

cv2.imshow("Pic-1",pic1)
cv2.imshow("Pic-2",pic2)
cv2.imshow("And",AndOp)
cv2.imshow("Or",OrOp)
cv2.imshow("Xor",XorOp)
cv2.imshow("Not",NotOp)

cv2.waitKey(0)
cv2.destroyAllWindows()