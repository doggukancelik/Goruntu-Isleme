import cv2
import numpy as np

canvas = np.zeros((512,512,3) , dtype=np.uint8) + 255  # tual oluşturduk 255 ile beyaz oldu

font1 = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_COMPLEX


cv2.putText(canvas , "DogukanBaba" , (100,100) , font2 , 4 , (0,0,0)  ,cv2.LINE_AA)



cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
