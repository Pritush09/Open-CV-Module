# Project to convert the image into grey scale and save ot for the usser
import cv2
#Taking the location input
a = input("Enter the location of the image : ")
img = cv2.imread(a,0)
img = cv2.resize(img,(560,400))
cv2.imshow("Grey Scale image ",img)

# In Order to save the image for the user
# 1-> take the waitkey in a variable
k = cv2.waitKey(0)
# 2-> check if the user press the input s as the key if it is s then save the image at the loaation with the given name
if k == ord('s'):
    cv2.imwrite("C:\\Users\\mynam\\Downloads\\goku_grey_scale_after_conversion.jpg",img)
else:
    cv2.destroyAllWindows()