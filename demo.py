import cv2
img = cv2.imread("C:\\Users\\mynam\\Downloads\\goku.jpg")
img = cv2.resize(img,(1280,800))# width , height
print(img)
print("\n")
cv2.imshow('original',img) # original to show the image in this window
cv2.waitKey()
cv2.destroyALLWindows()





