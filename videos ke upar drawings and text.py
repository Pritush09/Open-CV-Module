import cv2 
import numpy as np
import datetime

# this is with the videos 
# cap = cv2.VideoCapture("C:\\Users\\mynam\\Downloads\\Camaro SS Drifting Green Screen Footage - Trim.mp4")

# this is with the webcam
cap = cv2.VideoCapture(0)



print("Width : ",cap.get(3)) # 3 is for the width  Otherwise write cv2.CAP_PROP_FRAME_WIDTH
print("Height : ",cap.get(4)) # 4 is for the height  Otherwise write cv2.CAP_PROP_FRAME_HEIGHT


# we can also print this datatime.datetime.now to fetch the data time data 

while (cap.isOpened()):
    ret , frame = cap.read()
    frame = cv2.resize(frame,(800 , 500))
    if ret == True:
        
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        # this accepts  ( image  ,  text  , start_cordinaate  ,  font  ,  fontsize  ,  color  ,  thickiness  ,  linetype )
        frame = cv2.putText(frame , "CAR DRIFT height : {} width : {}".format(cap.get(4), cap.get(3)), (210,410) , font , 1 , (0,125,255) , 2, cv2.LINE_AA)
        
        
        frame = cv2.rectangle(frame , (0,100) , (200,400) , (154,92,44) , 3)  # color format BGR

        
        cv2.imshow("frame",frame)
        
        if cv2.waitKey(25) & 0xFF == ord("s"):
            break
    
    else:
        break


cap.release()
cv2.destroyAllWindows()
            
    
