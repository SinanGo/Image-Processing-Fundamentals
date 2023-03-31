import cv2

cam = cv2.VideoCapture(0)

width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))   # get width and height
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT)) # of the camera

print(width,height)

# fourcc -> four character code

myFourcc = cv2.VideoWriter_fourcc(*'MP4V')

# parameters : name of the record, fourcc, fps, shape
writer = cv2.VideoWriter("MyRecord.mp4",myFourcc,20,(width,height))

while True:
    
    ret, frame = cam.read() # get frame from the camera every 250 millisecond
    
    writer.write(frame) # add the frame to the record
    
    cv2.imshow("My Record",frame) # it is just to show what is going on
    
    if cv2.waitKey(250) & 0xFF == ord("q"):
        break

# with cv2.waitKey(250) and fps=20, we capture the frame every 250 milliseconds
# meaning that we get 4 frames per second

# FPS(frames per second) should be equal to 4 if we want to record a video having the same speed.

cam.release()
cv2.destroyAllWindows()