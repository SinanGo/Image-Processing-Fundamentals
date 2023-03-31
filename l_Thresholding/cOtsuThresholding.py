import cv2

image=cv2.imread("FingerPrint.jpg",0)

#simple thresholding
ret, simpleThresholding = cv2.threshold(image,127,255,cv2.THRESH_BINARY)

#otsu thresholding
ret, otsuThresholding = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("original",image)
cv2.imshow("simple threshold",simpleThresholding)
cv2.imshow("otsu",otsuThresholding)


cv2.waitKey(0)
cv2.destroyAllWindows()