#serit takibi

import cv2
import numpy  as  np

img = cv2.imread("chess.jpg")
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

edges= cv2.Canny(gray , 75 ,150)
lines = cv2.HoughLinesP(edges , 1,np.pi/180,50 , maxLineGap=40)

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img , (x1,y1) , (x2,y2), (0,255,0),2)

cv2.imshow("edge", edges)
cv2.imshow("img" , img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#for video

vid = cv2.VideoCapture("video.mp4")

while True:
    ret , frame =vid.read()
    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([18,94,140] , np.uint8)
    upper_yellow = np.array([48,255,255] , np.uint8)
    mask = cv2.inRange(hsv , lower_yellow,upper_yellow)
    edges = cv2.Canny(mask , 75,250)
    #bla bla udemy opencv kursu look.

#circle_Detection 

