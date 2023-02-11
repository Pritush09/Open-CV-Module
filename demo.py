import cv2
# format of image is bgr
#import numpy as np
img = cv2.imread("C:\\Users\\mynam\\Downloads\\goku.jpg",1) # 1 is default
# this 1 reperesents that the image will be read in colourfull manner 
img = cv2.resize(img,(1280,800))# width , height
# img = np.linspace(-10,10,9999).reshape(1111,3,3) this is just for the practice 
print(img)
print(img.shape)
cv2.imshow("original",img)
print("\n")


# To read the image in grey sacle mode
img = cv2.imread("C:\\Users\\mynam\\Downloads\\goku.jpg",0)
# this 0 reperesents that the image will be read in greyscale manner 
img = cv2.resize(img,(1280,800))# width , height
print(img)
print(img.shape)
cv2.imshow('Grey scale',img)

print("\n")

# too keep the image unchanged where the saturation value is little bit higher
img = cv2.imread("C:\\Users\\mynam\\Downloads\\goku.jpg",-1)
# this 0 reperesents that the image will be read in greyscale manner 
img = cv2.resize(img,(1280,800))# width , height
print(img)
print(img.shape)
cv2.imshow('unchanged',img)

# flip function 
img = cv2.flip(img,1) # this takes arg which are 0, 1 , -1 
cv2.imshow("Flipped",img)
# this function simply flips the image in different manner


cv2.waitKey() # default 0 -> meaing u have to close the img 
# this function takes time in milli seconds to hold the image on the screen
# other vise give the time in milliseconds format 3k-> 3sec

cv2.destroyAllWindows()




