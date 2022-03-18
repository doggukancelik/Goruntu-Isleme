#renkleri rgb , hsv , gray scale yapicaz. Çok önemli

import cv2
img  = cv2.imread("resim.jpg")   #okurken bgr okur

rgb = cv2.cvtColor(img , cv2.COLOR_BGR2RGB) # bgr -> rgb olur
hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)


cv2.imshow("real" , img)
cv2.imshow("rgb" , rgb)
cv2.imshow("hsv" , hsv)
cv2.imshow("gray" , gray)




#video için yapalım.

#videoCapture
#okuma kısmı
#frame = gray scale falan yap.

cv2.waitKey(0)
cv2.destroyAllWindows()