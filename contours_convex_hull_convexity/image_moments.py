import cv2
import numpy  as  np

img = cv2.imread("apple.jpg")
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray , 127,255,cv2.THRESH_BINARY)
#agirlik merkezi bulma
M = cv2.moments(thresh)
x= int(M["m10"]/M["m00"])
y= int(M["m01"]/M["m00"])
cv2.circle(img , (x,y) ,5,(255,255,0),-1)
cv2.imshow("img" , img)


#RESMIN ALANI VE CEVRESİ DE BULUNABİLİR.


cv2.waitKey(0)
cv2.destroyAllWindows()