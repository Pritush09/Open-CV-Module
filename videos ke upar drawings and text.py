import cv2 
import numpy as np
import datetime

cap = cv2.VideoCapture("C:\\Users\\mynam\\Downloads\\Camaro SS Drifting Green Screen Footage - Trim.mp4")

print("Width : ",cap.get(3)) # 3 is for the width  Otherwise write cv2.CAP_PROP_FRAME_WIDTH
print("Height : ",cap.get(4)) # 4 is for the height  Otherwise write cv2.CAP_PROP_FRAME_HEIGHT


while (cap.isOpened()):
    ret , frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        # this accepts  ( image  ,  text  , start_cordinaate  ,  font  ,  fontsize  ,  color  ,  thickiness  ,  linetype )
        frame = cv2.putText(frame , "CAR DRIFT" , (210,410) , font , 2 , (0,125,255) , 5 , cv2.LINE_AA)
        cv2.imshow("frame",frame)
        
        if cv2.waitKey(25) & 0xFF == ord("s"):
            break
    
    else:
        break


cap.release()
cv2.destroyAllWindows()
            
    
