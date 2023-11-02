import cv2
import numpy as np
from gfd.py.video.capture import VideoCaptureThreading

cv2.startWindowThread() #make the window
cap = VideoCaptureThreading(cv2.CAP_V4L2) # Start the Capture

cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
cap.set(cv2.CAP_PROP_FPS, 24)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

Person_cascade = cv2.CascadeClassifier("Desktop/haarcascade_upperbody.xml")

cap.start()
while True:

    ret, frame = cap.read() # Read the input video/stream
    gray = cv2.cvtColor(np.float32(frame), cv2.COLOR_BGR2GRAY) # Make the Frame gray
    gray = cv2.threshold(gray,70,255,0) 
    # read haacascade to detect people in input image

    # detects people in the input image
    gray = np.array(gray, dtype = 'uint8')
    People = Person_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE) # Find People in the Image
    print('Number of detected People:', len(People))

    # loop over all the detected people
    for (x,y,w,h) in People:
        #To draw a rectangle around the detected person  
        cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,255),2)
        
    cv2.imshow('Output', gray) # Display the Frame

cap.stop()
cap.release()
cv2.destroyAllWindows()
