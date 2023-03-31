import cv2

picture = cv2.imread("checkerboard.jpg")

cv2.imshow("Checkerboard",picture)

print("picture shape (height, width, channel count) :",picture.shape)

print(picture[(250,60)]) # 250 pixels down, 60 pixels right
print(picture[(275,275)]) # print bgr values

cv2.waitKey(0)
cv2.destroyAllWindows()