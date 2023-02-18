import cv2



def cor_pxcolor(event , x , y , flags , param):
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.putText(img , "X : {} Y : {}".format(y,x), (x-90,y+50) , font , 1 , (155,125,255) , 2, cv2.LINE_AA)
        cv2.imshow("IMG",img)
    
    elif event== cv2.EVENT_RBUTTONDOWN:
        b = img[y,x,0] #as blue channel is 0
        g = img[y,x,1] # as green value is 1
        r = img[y,x,2] # as red value is 2 
        
        color = str(b)+','+str(g)+','+str(r)
        cv2.putText(img , color, (x-90,y+50) , font , 1 , (155,125,255) , 2, cv2.LINE_AA)
        cv2.imshow("IMG",img)
        
        
        
cv2.namedWindow(winname="IMG")


img = cv2.imread("C:\\Users\\mynam\\Downloads\\goku.jpg",1) # 1 is default
img = cv2.resize(img,(900,690))
cv2.setMouseCallback("IMG",cor_pxcolor)# this is to join the function and our image (img)


while 1:
    cv2.imshow("IMG",img)
    
    if cv2.waitKey(1) & 0xFF == 27: # 27 is for the esc key to terminate 
       break 

cv2.destroyAllWindows()