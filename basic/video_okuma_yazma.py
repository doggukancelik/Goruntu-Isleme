import cv2

# 0
# video ismi
cap = cv2.VideoCapture(0)   # yukarıdaki parametreler ile yakalama işlemi yapabiliriz


while True:
    ret, frame = cap.read()
# if video bittiği an
    if ret ==0 :
        break
# endif


    frame = cv2.flip(frame , 1)  # y eksenine göre tersi flip 1

    cv2.imshow("Webcam", frame)  # Webcam yerine her şey olabilir.
    if cv2.waitKey(1) & 0xFF == ord("w"):      # tuşa basıldığı an dursun.
        break

cap.release()
cv2.destroyAllWindows()

