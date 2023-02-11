import cv2

# laptop ka camera ke liye 0 
# extrenal camera ke liye 1 
cap = cv2.VideoCapture(0)#,cv2.CAP.DSHOW) # the 0 means the web cam 
""" if there is a warning then we have to add this line as an argument it arrises only due to the python versons"""



# DIVX , XVID , MJPG , G264 , WMV1 , WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID") #XVID  it is widely suggested to save the video in this manner
# this is the helper that tells how u want to save the video in which format 



# it contains 4 parameter name, codec , fps , resolution
output = cv2.VideoWriter("C:\\Users\mynam\Downloads\first_vid_capture.avi",fourcc,20.0,(680,480))# ,0) 
# if uwant to save a grey scale video then u have to tell the output that the frames which are comming are grey scalled video







# cap is an object 
print('cap : ', cap)

while cap.isOpened(): # to check if the camera is opened or closed
     ret , frame = cap.read() # ret is for the knowledge that the video was read succesfully
     
     
     # now untill the camera is closed the ret value will be true so we have to check the ret value the below code will run 
     if ret == True:
         # to resize the frames 
         #frame = cv2.resize(frame,(700,450))   
         # above thing is not required as the resolution is fixed by us in the the above videowiter statement
         
         # if want to convert the video into the grey sacle video
         gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
         
         cv2.imshow("Frame",frame)
         cv2.imshow("Gray",gray)
         
         # this is to write the frames or save the video in the specified directory
         output.write(frame)  
         # if u want to save the gray scalled video then just pass the gray to the required in the output container
         
         
         
         # we gave 25 as to display the frames within at the interval of 25 mili seconds
         # jitni waitkey ki value kaam utna video fast
         # agar zero tab sirf diaplay hoga image video ka 
         k = cv2.waitKey(25) # to taking a key input and compare to stop the video
         
         # we did inorder to stop the video playing 
         if k==ord('s') & 0xFF: 
             # this 0xff it is mask so if there is a problem while playing it will automaticaly terminate the video
             break
         
cap.release()


# u have to release the ouput container which u have made inoder to doo this task without any problem ex.. the video maybe corrupt
output.release()


cv2.destroyAllWindows()