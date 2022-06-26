import cv2
import numpy  as  np

img = cv2.imread("apple.jpg")
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray , 127 , 255 ,cv2.THRESH_BINARY)
countours,_ = cv2.findContours(thresh , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img , countours , -1 , (0,0,255) ,3)
cv2.imshow("countour" , img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(countours)

