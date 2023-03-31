import cv2

image = cv2.imread("Rainbow.jpg",0)

ret, simpleThresholding = cv2.threshold(image, 127,255,cv2.THRESH_BINARY) # [0,127] -> 0 , [127,255] -> 255
ret, simpleThresholding2 = cv2.threshold(image, 127,255,cv2.THRESH_BINARY_INV)
ret, simpleThresholding3 = cv2.threshold(image, 127,255,cv2.THRESH_TOZERO) # [0,127] -> 0 , [127,255] -> [127,255]
ret, simpleThresholding4 = cv2.threshold(image, 127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow("Original",image)
cv2.imshow("Simple Thresholding 1",simpleThresholding)
cv2.imshow("Simple Thresholding 2",simpleThresholding2)
cv2.imshow("Simple Thresholding 4",simpleThresholding3)
cv2.imshow("Simple Thresholding 5",simpleThresholding4)

cv2.waitKey(0)
cv2.destroyAllWindows()

