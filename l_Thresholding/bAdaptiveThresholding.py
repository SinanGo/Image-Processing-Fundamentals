import cv2

image = cv2.imread("FingerPrint.jpg",0)

ret, simpleThresHolding = cv2.threshold(image, 150,255, cv2.THRESH_BINARY)

adaptiveThresholdingMean=cv2.adaptiveThreshold(image,200,cv2.ADAPTIVE_THRESH_MEAN_C,
                              cv2.THRESH_BINARY,5,2)
    
adaptiveThresholdingGaussian=cv2.adaptiveThreshold(image,200,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                              cv2.THRESH_BINARY,5,2)

cv2.imshow("Original", image)
cv2.imshow("Simple Thresholding",simpleThresHolding)
cv2.imshow("Adaptive Mean Thresholding", adaptiveThresholdingMean)
cv2.imshow("Adaptive Gaussian Thresholding",adaptiveThresholdingGaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()