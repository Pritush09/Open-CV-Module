import cv2
cap = cv2.VideoCapture("C:\\Users\mynam\Downloads\Camaro SS Drifting Green Screen Footage - Trim.mp4")
# cap is an object 
print('cap : ', cap)

while 1:
     ret , frame = cap.read() # ret is for the knowledge that the video was read succesfully
     
     # to resize the frames 
     frame = cv2.resize(frame,(700,450))
     
     # if want to convert the video into the grey sacle video
     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     
     cv2.imshow("Frame",frame)
     
     
     k = cv2.waitKey(25) # to taking a key input and compare to stop the video
     
     # we did inorder to stop the video playing 
     if k==ord('s') & 0xFF: 
         # this 0xff it is mask so if there is a problem while playing it will automaticaly terminate the video
         break
         
cap.release()
cv2.destroyAllWindows()
