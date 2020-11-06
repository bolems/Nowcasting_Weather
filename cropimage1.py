import cv2
img = cv2.imread('C:/Users/hp/Desktop/abc/prev2.jpg')
crop_img = img[0:690, 0:520]
#cv2.imshow("original", img)
#cv2.imshow("cropped", crop_img)
filenm = 'cp.jpg'
cv2.imwrite(filenm, crop_img)
cv2.waitKey(0)