import cv2 
import numpy as np
import datetime

cap = cv2.VideoCapture("C:\\Users\\mynam\\Downloads\\Camaro SS Drifting Green Screen Footage - Trim.mp4")

#print("Width : ",cap.get(3)) # 3 is for the width 
#print("Height : ",cap.get(4)) # 4 is for the height s


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
            
    
