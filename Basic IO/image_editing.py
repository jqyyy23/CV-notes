import os
import cv2

img = cv2.imread(os.path.join(".", "plane.jpg"))

#resize
resized_img = cv2.resize(img, (960, 596))

#crop
cropped_img = img[300:850, 0:1500] #only shows plane

print(img.shape)

cv2.imshow('image', img)
cv2.imshow('resized_image', resized_img)
cv2.imshow('cropped_imgage', cropped_img)
cv2.waitKey(0)