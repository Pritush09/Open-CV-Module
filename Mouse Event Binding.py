import cv2
import numpy as np

# X , Y are the position of your cursour on the windows created with the namedWindow 
# event is for the event performed by us like double click on either right or left  
def draw(event , x ,y , flags , param ):
    
    print("X : ",x)
    print("Y : ",y)
    print("\n")
    print("Flags : ",flags) # this value becomes 1 when we perform any of the task given in the if and elif statemetnt below
    print("\n")
    print("param : ",param)
    
    
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img , (x,y) , 100 , (125 , 0,255) , 4)
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.rectangle(img , (x,y) , (x+100,y+75) , (125,0,255) , 3)
    
# this will create a windows for our task with this name which will be used throughout
cv2.namedWindow(winname="VID")

# np.zeros is to create a img for us with black pixels
img = np.zeros([512,512,3])

cv2.setMouseCallback("VID",draw)# this is to join the function and our image (img)

while 1:
    cv2.imshow("VID",img)
    
    if cv2.waitKey(1) & 0xFF == 27: # 27 is for the esc key to terminate 
       break 

cv2.destroyAllWindows()

