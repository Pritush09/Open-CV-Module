import cv2
import numpy as np

img = cv2.imread("C:\\Users\\mynam\\Downloads\\goku.jpg")
img = cv2.resize(img,(840,680))


# here the line accepts 5 args (img , starting , ending , color , thickiness)
img = cv2.line(img , (0,0) , (200,200) , (154,92,44) , 9)  # color format BGR
# inorder to get the required color goo to google and search for online colour picker


# for the arrowed line
img = cv2.arrowedLine(img , (0,0) , (400,460) , (154,92,44) , 9)  # color format BGR


# Rectangle
img = cv2.rectangle(img , (0,100) , (200,400) , (154,92,44) , -1)  # color format BGR
#img = cv2.rectangle(img , (0,100) , (200,400) , (154,92,44) , 0)  # color format BGR

# if the thickness is a negative number then the shape will be filled with the colour of the line 



# circle img , center point  ,  radius , colour thickness
img = cv2.circle(img , (600,400) , 70 , (154,92,44) , 5)  # color format BGR
# if the thickness is a negative number then the shape will be filled with the colour of the line 





# FOR THE TEXT ON IMAGE
font = cv2.FONT_ITALIC
# this accepts  ( image  ,  text  , start_cordinaate  ,  font  ,  fontsize  ,  color  ,  thickiness  ,  linetype )
img = cv2.putText(img , "GOKU" , (210,410) , font , 2 , (0,125,255) , 5 , cv2.LINE_AA)




# for the ellipse  (image, center_coordinates, axesLength(major axes , minor axes), angle, startAngle, endAngle, color, thickness)
img = cv2.ellipse(img , (400,400) , (60, 40) , 90 , 90 , 270, (255,9,55) , 5) 





cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()