import cv2

pic1 = cv2.imread("cemYilmaz.jpg")
pic2 = cv2.imread("ozanGuven.jpg")

# normal sum-1
print(pic1[0,0]) # 207,207,205
print(pic2[0,0]) # 102,99,84
print(pic1[0,0]+pic2[0,0]) # (207+102)%256, (207+99)%256, (205+84)%256
                           # 53,50,33 ---> typical unsigned integer sum

# normal sum-2
print(pic1[95,95]) # 126,143,150
print(pic2[95,95]) # 119,143,185
pic3 = cv2.add(pic1,pic2) # min[255,(126+119)],min[255,(143+143)],min[255,150+185]
                          # 245,255,255 ---> the image can have at most a white color (255,255,255)
print(pic3[95,95]) 

# weighted sum
pic4 = cv2.addWeighted(pic1,0.3,pic2,0.7,0) # add pictures with their given weights

cv2.imshow("Cem",pic1)
cv2.imshow("Ozan",pic2)
cv2.imshow("Sum",pic3)
cv2.imshow("Weighted Sum",pic4)

cv2.waitKey(0)
cv2.destroyAllWindows()