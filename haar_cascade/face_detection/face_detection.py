import  cv2
img = cv2.imread("face.jpg")
face_cascade = cv2.CascadeClassifier("frontalface.xml")

gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray , 1.3,4) # 4 kare  . yanlışlık varsa değiştir


#çizim kısmı
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)


cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

##################################################
#video
"""
import cv2
vid = cv2.VideoCapture("video_yolu")
face_cascade = cv2.CascadeClassifier("frontalface.xml")

while 1 :
    _,frame=vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.3,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow("image", img)
    if cv2.waitKey(5) & 0xFF ==ord("q"):
        break

vid.release()
cv2.destroyAllWindows()
"""
#######################################################
