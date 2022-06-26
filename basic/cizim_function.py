import cv2
import numpy as np

canvas = np.zeros((512,512,3) , dtype=np.uint8) + 255  # tual oluşturduk 255 ile beyaz oldu


# cizgi cizme islemi
cv2.line(canvas , (50,50) , (512,512) , (255,0,0), thickness=5) # tual , başlangic , bitis , renk , kalınlık

# dortgen cizimi
cv2.rectangle(canvas , (20,20) , (50,50) , (0,255,0) ,thickness=2)

# cember cizimi
cv2.circle(canvas , (250,250) , 150 ,(0,200,0),thickness=-1)  #-1 dolu , pozitif kalınlık

# ucgen cizimi
p1 = (100,200)
p2 = (50,50)
p3 = (300,100)
cv2.line(canvas , p1,p2,(0,0,0) , 4)
cv2.line(canvas , p2,p3,(0,0,0) , 4)
cv2.line(canvas , p3,p1,(0,0,0) , 4)


#cokgen cizimi
points = np.array([[110, 200], [330, 200], [290,220], [220, 250], [400,420]], np.int32)
cv2.polylines(canvas, [points], isClosed=True, color=(0, 0, 100), thickness=5)



cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()