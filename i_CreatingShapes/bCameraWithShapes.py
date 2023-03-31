import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, image = cam.read()

    cv2.imshow("My Camera", image)

    cv2.rectangle(image,(100,100),(400,400),(150,150,150),10)
    cv2.line(image,(0,0),(100,100),(0,0,255),2)
    cv2.circle(image,(150,150),40,(255,0,0),5)
    cv2.putText(image,"circle",(115,150),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)


    cv2.imshow("My Camera with Shapes",image)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()