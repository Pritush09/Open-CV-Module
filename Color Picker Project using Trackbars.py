import cv2
import numpy as np

# blank image
img  = np.zeros([300,512,3],np.uint8)
cv2.namedWindow("COLOR PICKER")



#create switch
def c(x):
    pass

s = "0 : OFF \n 1 : ON"
#iska format he (sting jo dikhana he  , Konsa window pe , start value , end value , konsa function (default he cross) ,  ) 
cv2.createTrackbar(s , "COLOR PICKER" , 0 , 1 , c )


""" this  c is a function which will be called in the free time when the trackbar is not being used """


# creating for RGB
cv2.createTrackbar('R' , "COLOR PICKER" , 0 , 255 , c )
cv2.createTrackbar('G' , "COLOR PICKER" , 0 , 255 , c )
cv2.createTrackbar('B', "COLOR PICKER" , 0 , 255 , c )




while 1:
    cv2.imshow("COLOR PICKER",img)
        
    k = cv2.waitKey(1) & 0xFF
    if k == 27:#esc
        break
    
    
    
    # now  get trackbar position 
    s1 =  cv2.getTrackbarPos(s,"COLOR PICKER")
    r =  cv2.getTrackbarPos('R',"COLOR PICKER")
    g =  cv2.getTrackbarPos("G","COLOR PICKER")
    b =  cv2.getTrackbarPos("B","COLOR PICKER")
    
    
    if s1==0:
        img[:] = 0
    else:
        img[:] = [r,g,b]
        
cv2.destroyAllWindows()