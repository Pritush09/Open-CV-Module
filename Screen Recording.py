# Screen Recording 

import cv2 as c
import pyautogui as p


# we will capture the resolution of aur screen 
screen_res = p.size()  # screen ka size batadega


# take the input for the file name in which we will store the recording
fname = input("Enter the filename in which the recording will be saved (path): ")

# seting the fps
fps = 60.0

fourcc = c.VideoWriter_fourcc(*"XVID")
output = c.VideoWriter(fname,fourcc,fps,screen_res)# ,0) #agar grey scale me lana he video ko





