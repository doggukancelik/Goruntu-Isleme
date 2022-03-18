import cv2
import numpy

img = cv2.imread("resim.jpg")


dimension = img.shape
print(dimension)

#renkleri görme
color = img[150,200]  # resmin 150 200 pixelindeki rengi verir    #bgr
blue = img[150,200 , 0] # blue rengi verir
green = img[150,200 , 1] # green rengi verir
red = img[150,200 , 2] # red rengi verir

#renk değiştirme
img[150,200,0] = 250   #mavi 250 yaptık
#yada
blue_degeri = img.item(150,200,0)
new_blue = img.itemset((150,200,0) , 172)



cv2.imshow("resimx" , img)
cv2.waitKey(0)

cv2.destroyAllWindows()