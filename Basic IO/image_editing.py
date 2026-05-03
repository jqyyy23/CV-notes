import os
import cv2

img = cv2.imread(os.path.join (".", "CV-notes", "Basic IO", "plane.jpg"))

#resize
resized_img = cv2.resize(img, (960, 596))

#crop
cropped_img = img[300:850, 0:1500] #only shows plane

#colorspace change
rbg_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #switched blue and red
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #grayscale (condensing 3 channels to 1 channel)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #hsv: hue, saturation, value; helps with color detection 

#blurring (each pixel is replaced by the average of the pixels around it, its 'neighbourhood', useful for removing noise)
kernal_size = 15
img_blur = cv2.blur(img, (kernal_size, kernal_size))
img_Gblur = cv2.GaussianBlur(img, (kernal_size, kernal_size), 6)
img_median_blur = cv2.medianBlur(img, kernal_size) #always square size

#threshold (convert grayscale to binary using a threshold value, useful for image segmentation)
ret, thresh = cv2.threshold(img_gray, 150, 225, cv2.THRESH_BINARY) #ret is assigned threshold value, can be optimized
ret2, thresh2 = cv2.threshold(img_gray, 0, 225, cv2.THRESH_BINARY + cv2.THRESH_OTSU) #auto-calculates optimal threshold value
ret3, thresh3 = cv2.threshold(cv2.cvtColor((img_median_blur), cv2.COLOR_BGR2GRAY), 50, 255, cv2.THRESH_BINARY) #using blurred version 
adapt_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 20) #21 is block size, needs to be odd. Adaptive breaks image into segments with own threshold

#edge detection (3 types: Sobel Derivatives, Laplace Operator, Canny Edge Detector)
img_edge = cv2.Canny(img, 250, 100) # max & min

cv2.imshow('image', img)
# cv2.imshow('resized_image', resized_img)
# cv2.imshow('cropped_imgage', cropped_img)
# cv2.imshow('rbg_img', rbg_img)
# cv2.imshow('img_gray', img_gray)
# cv2.imshow('img_hsv', img_hsv)
# cv2.imshow('img_blur', img_blur)
# cv2.imshow('img_Gblur', img_Gblur)
# cv2.imshow('img_median_blur', img_median_blur)
# cv2.imshow("thresh", thresh)
# cv2.imshow("thresh2", thresh2)
# print(ret2)
# cv2.imshow("thresh3", thresh3)
# cv2.imshow("adapt_thresh", adapt_thresh)
cv2.imshow("img_edge", img_edge)
cv2.waitKey(0)