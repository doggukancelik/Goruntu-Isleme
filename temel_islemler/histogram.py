import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((500,500) , np.uint8)
#cv2.imshow("img" , img)
cv2.rectangle(img , (0,60), (200,150) , (255,255,255) , -1)
cv2.rectangle(img , (70,260), (300,400) , (255,255,255) , -1)

plt.hist(img.ravel() , 256 , [0,256])
#plt.show()

img1 =cv2.imread("1.PNG")
cv2.imshow("renkli resim" , img1)
b , g, r = cv2.split(img1)
plt.hist(b.ravel() , 256 , [0,256])
plt.hist(g.ravel() , 256 , [0,256])
plt.hist(r.ravel() , 256 , [0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()