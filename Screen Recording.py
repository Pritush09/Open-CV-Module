# Screen Recording 

import cv2 as c
import pyautogui as p
import numpy as np

# we will capture the resolution of aur screen 
screen_res = p.size()  # screen ka size batadega


# take the input for the file name in which we will store the recording
fname = input("Enter the filename in which the recording will be saved (path): ")

# seting the fps
fps = 20.0

fourcc = c.VideoWriter_fourcc(*"XVID")
output = c.VideoWriter(fname,fourcc,fps,screen_res)# ,0) #agar grey scale me lana he video ko


#creating our own window #create recording module
c.namedWindow("Live_recording",c.WINDOW_NORMAL)
# resizing the window
c.resizeWindow("Live_recording",(600,400))

while 1:
    img = p.screenshot()# this will continuously take the ss of screen and store it in img
    f = np.array(img) # storing the capturedimage in an numpy array
    f = c.cvtColor(f,c.COLOR_BGR2RGB)#this is to change the color of the image captured
    # isko rgb me convert karna pada as the opencv reads an image as BGR but in computer it we see BGR
    
    #saving
    output.write(f)
    
    c.imshow("Live_recording",f) # naam hamesha same hona chaiye 
    # varna dikat hoga 
    
    k = c.waitKey(1) # to taking a key input and compare to stop the video
    
    # we did inorder to stop the video playing 
    if k==ord('s') & 0xFF: 
        # this 0xff it is mask so if there is a problem while playing it will automaticaly terminate the video
        break
    
    
output.release()

c.destroyAllWindows()