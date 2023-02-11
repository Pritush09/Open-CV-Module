import cv2
import numpy as np
img = cv2.imread("C:\\Users\\mynam\\Downloads\\goku.jpg")
#img = cv2.resize(img,(1280,800))# width , height
img = np.linspace(-10,10,9999).reshape(1111,3,3)
print(img)
print(img.shape)
print("\n")
cv2.imshow('original',img) # original to show the image in this window
cv2.waitKey()





