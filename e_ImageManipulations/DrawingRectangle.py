import cv2

pic = cv2.imread("ImageToManipulate2.jpg")

# draw a rectange on the pic by giving two opposite points
cv2.rectangle(pic,(50,100),(160,150),[0,255,0],2)
# source, p1(x1,y1), p2(x2,y2),color,thickness

cv2.imshow("Eyes",pic)

cv2.waitKey(0)
cv2.destroyAllWindows()