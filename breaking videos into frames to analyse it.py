import cv2

vcap = cv2.VideoCapture("C:\\Users\\mynam\\Downloads\\Camaro SS Drifting Green Screen Footage.mp4")

ret , image = vcap.read()# read the frames or video

count = 0 

while 1:
    if ret == True:
        
        cv2.imshow("res",image)
        
        
        count += 1
        
        if cv2.waitKey(1) & 0xFF == ord("s"):
            break
            cv2.destroyAllWindows()
            
vcap.release()
cv2.destroyAllWindows()