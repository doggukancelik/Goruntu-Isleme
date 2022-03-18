#roi  = isimiz gözle ise resmin sadece göz kısmını alır. kırpma işlemi gibi

import cv2
img = cv2.imread("resim.jpg")

cv2.imshow("resimm" , img)

roi = img[30:200,200:300]  # veri seti kırpma gibi.
cv2.imshow("roi kısmı" , roi)
cv2.waitKey(0)
cv2.destroyAllWindows()