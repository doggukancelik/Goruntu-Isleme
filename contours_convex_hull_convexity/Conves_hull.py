import cv2
import numpy  as  np

img = cv2.imread("star.jpg")
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray , (3,3))
ret , thresh = cv2.threshold(blur , 250 ,255 , cv2.THRESH_BINARY)


cv2.imshow("img" , img)
cv2.imshow("gray" , gray)
cv2.imshow("blur" , blur)
cv2.imshow("thresh" , thresh)


countours , hiearchy = cv2.findContours(thresh , cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
hull = []


for i in range(len(countours)):
    hull.append(cv2.convexHull(countours[i], False))
bg = np.zeros((thresh.shape[0] , thresh.shape[1] ,3 ), np.uint8)

for i in range(len(countours)):
    cv2.drawContours(bg, countours , i , (255,0,0), 3 ,8 ,hiearchy)  #kenar
    cv2.drawContours(bg, hull , i , (0,255,0) , 1 ,8)  #ortu

cv2.imshow("bg" , bg)

cv2.waitKey(0)
cv2.destroyAllWindows()