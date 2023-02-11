import cv2

# laptop ka camera ke liye 0 
# extrenal camera ke liye 1 
cap = cv2.VideoCapture(0)#,cv2.CAP.DSHOW) # the 0 means the web cam 
""" if there is a warning then we have to add this line as an argument """

# cap is an object 
print('cap : ', cap)

while cap.isOpened(): # to check if the camera is opened or closed
     ret , frame = cap.read() # ret is for the knowledge that the video was read succesfully
     
     
     # now untill the camera is closed the ret value will be true so we have to check the ret value the below code will run 
     if ret == True:
         # to resize the frames 
         frame = cv2.resize(frame,(700,450))
         
         # if want to convert the video into the grey sacle video
         gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
         
         cv2.imshow("Frame",frame)
         cv2.imshow("Gray",gray)
         
         # we gave 25 as to display the frames within at the interval of 25 mili seconds
         # jitni waitkey ki value kaam utna video fast
         # agar zero tab sirf diaplay hoga image video ka 
         k = cv2.waitKey(25) # to taking a key input and compare to stop the video
         
         # we did inorder to stop the video playing 
         if k==ord('s') & 0xFF: 
             # this 0xff it is mask so if there is a problem while playing it will automaticaly terminate the video
             break
         
cap.release()
cv2.destroyAllWindows()