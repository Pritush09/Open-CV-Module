import cv2

vcap = cv2.VideoCapture("C:\\Users\\mynam\\Downloads\\first_vid.mp4")

ret , image = vcap.read()# read the frames or video
#this only captures the first frame of the video
count = 0 

while 1:
    if ret == True:
        
        cv2.imwrite("C:\\Users\\mynam\\FRAMES\\imgN{}.jpg".format(count),image)
        
        #this is to set that the speed of the capturing of the image
        vcap.set(cv2.CAP_PROP_POS_MSEC,(count**100))
        #Capture proportion position in milisecond
        # jo bhi count aega usko count**100 me set kardena aur fir utna mili second hone par ek frme save karna
        
        ret , image = vcap.read()# read the frames or video

        
        cv2.imshow("res",image)
        print(count)
        
        count += 1
        
        if cv2.waitKey(1) & 0xFF == ord("s"):
            break
            cv2.destroyAllWindows()
            
vcap.release()
cv2.destroyAllWindows()