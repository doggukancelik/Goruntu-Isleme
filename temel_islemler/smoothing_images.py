import cv2
import numpy as  np

# gurultu azalır
# blurlaştırma işlemidir.
#farklı çeşitlerini inceleyebilirsin.
#bitwise işlemler ile mantıksal karşılaştırma yapılır.

img_filter = cv2.imread("noisy.png")
img_median = cv2.imread("noisy.png")
img_bilateral = cv2.imread("noisy.png")

blur = cv2.blur(img_filter , (50,50))
median_blur = cv2.medianBlur(img_median , 9)



cv2.imshow("original" , img_filter)
cv2.imshow("blur" , blur)
cv2.imshow("median_blur",median_blur)

bit_or = cv2.bitwise_or(img_filter , blur)
cv2.imshow("karsilastirma" , bit_or)   # 0 siyah 1 beyaz

cv2.waitKey(0)
cv2.destroyAllWindows()