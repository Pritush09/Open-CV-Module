import cv2
import numpy as np

img = cv2.imread("C:\\Users\\mynam\\Downloads\\goku.jpg")
img = cv2.resize(img,(840,680))
cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()