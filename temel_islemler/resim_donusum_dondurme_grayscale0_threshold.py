import cv2
import numpy as np
#kirpma islemi
img = cv2.imread("resim.jpg" , 0 ) # 0 grayscale yapar
cv2.imshow("resim" , img)

row , col = img.shape
M = np.float32([[1,0,10] , [0,1,70]])
dst = cv2.warpAffine(img , M , (row,col))
cv2.imshow("dst" ,dst )

#dondurme islemi
X = cv2.getRotationMatrix2D((col/2, row/2),90,1)
dst_new = cv2.warpAffine(img, X , (col, row))
cv2.imshow("dondurme" , dst_new)


#threshold
ret , th1 = cv2.threshold(img , 150,255, cv2.THRESH_BINARY)
cv2.imshow("threshol" , th1)
th2 = cv2.adaptiveThreshold(img , 40, cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY,11 ,2 )
cv2.imshow("threshol2" , th2)


cv2.waitKey(0)
cv2.destroyAllWindows()