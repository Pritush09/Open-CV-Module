import cv2
# format of image is bgr
#import numpy as np
img = cv2.imread("C:\\Users\\mynam\\Downloads\\goku.jpg",1) # 1 is default
# this 1 reperesents that the image will be read in colourfull manner 
img = cv2.resize(img,(1280,800))# width , height
# img = np.linspace(-10,10,9999).reshape(1111,3,3) this is just for the practice 
print(img)
print(img.shape)
print("\n")


# To read the image in grey sacle mode
img = cv2.imread("C:\\Users\\mynam\\Downloads\\goku.jpg",0)
# this 0 reperesents that the image will be read in greyscale manner 
img = cv2.resize(img,(1280,800))# width , height
print(img)
print(img.shape)


cv2.imshow('original',img) # original to show the image in this window
cv2.waitKey(3000) # default 0 -> meaing u have to close the img 
# this function takes time in milli seconds to hold the image on the screen
# other vise give the time in milliseconds format 3k-> 3sec

cv2.destroyALLWindows()




