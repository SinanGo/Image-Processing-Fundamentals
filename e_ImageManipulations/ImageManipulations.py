import cv2

pic = cv2.imread("ImageToManipulate.jpg")

partOfPic = pic[50:200,50:200].copy()
# if we would write it as partOfPic = pic[50:200,50:200],
# every change in partOfPic would affect to pic.

cv2.imshow("part before",partOfPic)

partOfPic[:,:,0] = 255 # Blue Filter on Red Apple

cv2.imshow("part after",partOfPic)

pic[0:150,0:150] = partOfPic # write partOfPic to the given field of pic

cv2.imshow("Manipulated Pic",pic)


cv2.waitKey(0)
cv2.destroyAllWindows()