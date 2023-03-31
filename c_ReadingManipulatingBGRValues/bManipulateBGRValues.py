import cv2

picture = cv2.imread("checkerboard.jpg")

cv2.imshow("Before",picture)

for i in range(90): #draw a white line with a length of 90 pixels
    picture[30,i] = [255,255,255] 

for i in range(20,40):            # draw a red rectangle with
    for j in range(30,60):        # width of 20, length of 30 pixels.
        picture[i,j] = [0,0,255]  
                                  # start from [20,30]- 20 pixels down,30 pixels right
cv2.imshow("After",picture)

cv2.imwrite("checkerboard-2.jpg",picture)

cv2.waitKey(0)
cv2.destroyAllWindows()