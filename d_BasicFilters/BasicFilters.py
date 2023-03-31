import cv2

pic = cv2.imread("aldebaran22v3.jpg")

BlueFilteredPic = pic.copy()
GreenFilteredPic = pic.copy()
RedFilteredPic = pic.copy()
PurpleFilteredPic = pic.copy()

# the reason why we use copy() function is that we do not want to reference
# object on the left to the object on the right. We want to have a copy just like the original one.

# search for 'pass by value' and 'pass by reference' terms on google

BlueFilteredPic[:,:,0] = 255 # Change blue value as 255 for all pixels
GreenFilteredPic[:,:,1] = 255 
RedFilteredPic[:,:,2] = 255

# create a purple filtered field in two steps.
# purple = blue + red

# check the intervals

PurpleFilteredPic[150:230,560:600,0] = 255 # blue mask
                                           # change blue value as 255 for the pixels
                                           # in the given interval

PurpleFilteredPic[200:280,560:600,2] = 255 # red mask
                                           # change red value as 255 for the pixels
                                           # in the given interval

cv2.imshow("Blue filter",BlueFilteredPic)
cv2.imshow("Green filter",GreenFilteredPic)
cv2.imshow("Red filter",RedFilteredPic)
cv2.imshow("Purple filter",PurpleFilteredPic)

cv2.waitKey(0)
cv2.destroyAllWindows()