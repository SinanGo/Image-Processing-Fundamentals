import cv2

#reading
picture = cv2.imread("aldebaran22v1.jpg") # read and assign the picture to the variable
picture2 = cv2.imread("aldebaran22v1.jpg",0) #flag 0 : grayscale 

#showing
cv2.imshow("Aldebaran",picture) # open a window with 'Aldebaran' title
cv2.imshow("Aldebaran 2",picture2)

#writing
cv2.imwrite("New Picture.jpg",picture2) # create a jpg file with the spesified name

cv2.waitKey(0) # keep windows open until any key stroke
               # try running without this function

cv2.destroyAllWindows() # close all currently open windows created by
                        # the OpenCv functions like imshow