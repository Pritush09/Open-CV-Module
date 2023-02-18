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



# creating for RGB



