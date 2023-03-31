import cv2

cam = cv2.VideoCapture(0) # flag 0 : internal camera (as in laptops)
                          # flag 1 : external camera
                          # "url" : Specified video

while True:
    
    ret, image = cam.read() # ret is used for checking if camera works or not
    
    cv2.imshow("My Camera",image) # The image can be captured background.
                                  # We can also see what is going on with this statement.
    
    if cv2.waitKey(30) & 0xFF == ord('q'): # take an image every 30 milliseconds
        break                              # press q for terminating the program
                                           # what if we change 30 with something like 500?
                                           
cam.release() # release camera safely when it is not needed.
cv2.destroyAllWindows()