import cv2
img = cv2.imread('plasticbag2.jpeg')
print(img.shape)
imgResize = cv2.resize(img, (640,480))
imgCropped = img[0:200,200:500]
cv2.imshow("ImageResize", imgResize)
cv2.imshow("ImageCropped", imgCropped)
print(imgResize.shape)

cv2.waitKey(0)