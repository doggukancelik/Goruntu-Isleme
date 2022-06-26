import cv2

img =cv2.imread("resim.jpg")    #okuma işlemi ->matris şekline çevirdi.  0 = gri
# print(img)

cv2.namedWindow("Image" , cv2.WINDOW_NORMAL) # pencere hareketi
cv2.imshow("Image" , img)   #pencere oluşur.

# img=cv2.resize(img, (100,480))  # boyut ayarlama


cv2.imwrite("klon1.jpg", img)  # resim kapandıktan sonra bu oluşur.başka yere ise dosya uzantısı yaz.
cv2.waitKey(0)   # pencere 0 basınca kapanır
cv2.destroyAllWindows()

#aspect_ratio

