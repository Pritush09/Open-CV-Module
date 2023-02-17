import cv2 
import numpy as np


cap = cv2.VideoCapture("C:\\Users\\mynam\\Downloads\\Camaro SS Drifting Green Screen Footage - Trim.mp4")


while (cap.isOpened()):
    ret , frame = cap.read()
    if ret == True:
        cv2.imshow("frame",frame)
        
        if cv2.waitKey(25) & 0xFF == ord("s"):
            break
    
    else:
        break


cap.release()
cv2.destroyAllWindows()
            
    
