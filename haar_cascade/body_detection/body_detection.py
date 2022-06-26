import cv2
img = cv2.imread("body.jpg")
body_cascade = cv2.CascadeClassifier("fullbody.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bodies = body_cascade.detectMultiScale(gray , 1.1 ,1)

for(x,y,w,h) in bodies:
    cv2.rectangle(img,(x,y),(x+w,y+h) , (0,0,255) , 3)

cv2.imshow("i" , img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#####################################
#for video
import cv2

vid = cv2.VideoCapture("body.mp4")
body_cascade = cv2.CascadeClassifier("fullbody.xml")

while 1:
    ret,frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bodies = body_cascade.detectMultiScale(gray,1.1,4)

    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
    cv2.imshow("video" , frame)

    if cv2.waitKey(10) &0xFF ==ord("q"):
        break

vid.release()
cv2.destroyAllWindows()