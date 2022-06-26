import cv2

cap = cv2.VideoCapture(0 , cv2.CAP_DSHOW)
filename= "yol"
frameRate=30
resolution= (640,480)
codec = cv2.VideoWriter_fourcc('W','M','V',2)
videoFileOutput =cv2.VideoWriter(filename)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame , 1)  # y eksenine göre tersi flip 1
    videoFileOutput.write(frame)


    cv2.imshow("WebcamLive", frame)  # Webcam yerine her şey olabilir.
    if cv2.waitKey(1) & 0xFF == ord("w"):      # tuşa basıldığı an dursun.
        break

videoFileOutput.release()
cap.release()
cv2.destroyAllWindows()
#android için ip webcam indir. import request ile. Mantık aynı


