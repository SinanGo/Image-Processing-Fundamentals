import cv2
import numpy as np

pic = np.zeros((300,300,3), dtype="uint8")

# source, p1(x,y), p2(x,y), color, thickness
cv2.line(pic,(0,0),(100,100),(0,0,255),6)
cv2.imshow("Draw a Line", pic)

# source, center, radius(x,y), color, thickness
cv2.circle(pic,(150,150),10,(255,0,0),3)
cv2.imshow("Add a Circle", pic)

#source, string to write, starting point(x,y),font, font size, color, thickness 
cv2.putText(pic,"This is a text",(25,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),4)
cv2.imshow("Add a Text", pic)

cv2.waitKey(0)
cv2.destroyAllWindows() 


