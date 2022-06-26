import cv2
import numpy as np

#erosion
img = cv2.imread("resim.jpg",  0)
kernel = np.ones((5,5) , np.uint8)
erosion = cv2.erode(img,kernel , iterations=1)

#ex
img = cv2.imread("resim.jpg",  0)
kernel = np.ones((5,5) , np.uint8)
dilate = cv2.morphologyEx(img,cv2.MORPH_DILATE , kernel)

cv2.imshow("erosion" , erosion)
cv2.imshow("dilate" , dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()