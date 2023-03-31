import cv2

image = cv2.imread("NoisyPicture.jpg")

meanFilter1 = cv2.blur(image,(3,1))
meanFilter2 = cv2.blur(image,(4,4))
meanFilter3 = cv2.blur(image,(7,7))

medianFilter1 = cv2.medianBlur(image,3)
medianFilter2 = cv2.medianBlur(image,7)

gaussFilter1 = cv2.GaussianBlur(image,(3,3),0)

# observe pictures and see the differences
cv2.imshow("Original", image)
cv2.imshow("Mean 1",meanFilter1)
cv2.imshow("Mean 2",meanFilter2)
cv2.imshow("Mean 3", meanFilter3)
cv2.imshow("Median 1", medianFilter1)
cv2.imshow("Median 2", medianFilter2)
cv2.imshow("Gaussian 1", gaussFilter1)

cv2.waitKey(0)
cv2.destroyAllWindows()