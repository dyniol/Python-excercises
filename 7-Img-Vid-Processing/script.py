import cv2

img=cv2.imread("files/galaxy.jpg", 0) #import img

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2))) # how to resize img
cv2.imshow("Galaxy", resized_image) # how to show img
cv2.imwrite("Galaxy_resized.jpg", resized_image)
cv2.waitKey(0) 
cv2.destroyAllWindows()