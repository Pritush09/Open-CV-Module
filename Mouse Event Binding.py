import cv2
import numpy as np


def draw(event , x ,y , flags , param ):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img , (x,y) , 100 , (125 , 0,255) , 4)
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.rectangle(img , (x,y) , (x+100,y+75) , (125,0,255) , 3)
    
cv2.namedWindow(winname="VID")
img = np.zeros([512,512,3])

cv2.setMouseCallback("VID",draw)# this is to join the function and our image (img)

while 1:
    cv2.imshow("VID",img)
    
    if cv2.waitKey(1) & 0xFF == 27: # 27 is for the esc key to terminate 
       break 

cv2.destroyAllWindows()

