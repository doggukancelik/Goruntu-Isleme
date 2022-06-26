import cv2
import numpy as np

circle = np.zeros((512,512,3) , np.uint8) + 255
cv2.circle(circle , (256,256) , 60 , (255,0,0) , -1)

rectangle = np.zeros((512,512,3) , np.uint8) + 255
cv2.rectangle(rectangle , (150,150) ,(350,350) , (0,0,255) , -1)

cv2.imshow("c" , circle)
cv2.imshow("r" , rectangle)
#normal toplama
add = cv2.add(circle,rectangle)
cv2.imshow("add" , add)

#agirlikli toplama
dst = cv2.addWeighted(circle , 0.7 , rectangle , 0.3 , 0)  # circle 0.7 eklendi...
cv2.imshow("agirlikli" , dst)


cv2.waitKey(0)
cv2.destroyAllWindows()