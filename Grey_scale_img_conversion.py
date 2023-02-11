# Project to convert the image into grey scale and save ot for the usser
import cv2
#Taking the location input
a = input("Enter the location of the image : ")
img = cv2.imread(a,0)
img = cv2.resize(img,(560,400))
cv2.imshow("Grey Scale image ",img)
cv2.waitKey()