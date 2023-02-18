import cv2 
import numpy as np

img = cv2.imread("C:\\Users\mynam\Downloads\goku.jpg",1)
img = cv2.resize(img,(600,400))
cv2.imshow("img",img)

"""
print("shape",img.shape)
print("Size : ",img.size)
print("dtype : ",img.dtype)
print("type : ",type(img))
"""

b , g , r  = cv2.split(img)
"""
cv2.imshow("red",r)
cv2.imshow("green",g)
cv2.imshow("blue",b)
"""


mer1 = cv2.merge((b,g,r)) # in the format opencv undrstand
cv2.imshow("mer",mer1)
mer2 = cv2.merge((r,g,b))
cv2.imshow("rgb",mer2)
mer3 = cv2.merge((g,b,r))
cv2.imshow('gbr',mer3)
mer4=cv2.merge((g,r,b))
cv2.imshow("grb",mer4)

# doo the numpy indexing to fetch the data of a particular channel



cv2.waitKey(0)
cv2.destroyAllWindows()