import cv2
import numpy as np

img = cv2.imread("C:\\Users\\mynam\\Downloads\\goku.jpg")
img = cv2.resize(img,(840,680))


# here the line accepts 5 args (img , starting , ending , color , thickiness)
img = cv2.line(img , (0,0) , (200,200) , (154,92,44) , 9)  # color format BGR
# inorder to get the required color goo to google and search for online colour picker


# for the arrowed line
img = cv2.arrowedLine(img , (0,0) , (400,460) , (154,92,44) , 9)  # color format BGR



cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()