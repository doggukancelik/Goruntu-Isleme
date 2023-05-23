import cv2
import pickle
import cvzone
import numpy as np

#video
cap = cv2.VideoCapture('carPark.mp4')

########################################################################################################################
#1- Data türü ve yapısı:
def get_video_properties(video_path):
    # Videoyu aç
    video = cv2.VideoCapture(video_path)
    # Video özelliklerini al
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video.get(cv2.CAP_PROP_FPS)
    duration_sec = frame_count / fps
    # Video çözünürlüğünü al
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Videoyu kapat
    video.release()

    return frame_count, fps, duration_sec , width , height

video_path = 'carPark.mp4'
frame_count, fps, duration_sec ,width, height = get_video_properties(video_path)
# Sonuçlarıları yazdıralım:
print("***Çerçeve Sayısı:", frame_count , "***FPS:", fps , "***Süre (saniye):", duration_sec)
print("Çözünürlük: {}x{}".format(width, height))
########################################################################################################################

width , height = 107,48   #dikdörtgenin uzun ve kısa kenarını belirledik

def checkParkingSpace(imgPro):
    spaceCounter=0
    for pos in posList:
        x , y =pos

        imgCrop = imgPro[y:y+height,x:x+width]
        #cv2.imshow(str(x*y) , imgCrop)

        #oluşturulan dikdörtgen içinde ne kadar pixel dolu , çok ise ara vardır.
        count = cv2.countNonZero(imgCrop)
        cvzone.putTextRect(img , str(count) , (x,y+height-3) , scale= 1.5
                           ,thickness=2 , offset=0, colorR=(0,0,250))


        if count < 850:
            color= (0,255,0) #red
            thickness=5
            spaceCounter +=1
        else:
            color = (0,0,255) #green
            thickness = 5
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)

    #skorları yazdırmak için
    cvzone.putTextRect(img, f'Free :{spaceCounter}/{len(posList)}', (100, 50), scale=3
                       , thickness=5, offset=20, colorR=(0, 200, 0))

with open('CarParkPos', 'rb') as f:  # önceki dikdörtgenleri tutar
    posList = pickle.load(f)





while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):    #VİDEO HEP DEVAM EDER BU IF İLE
        cap.set(cv2.CAP_PROP_POS_FRAMES , 0)
    succes , img = cap.read()


    imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray , (3,3) , 1)
    #Binary image yapma
    imgThreshold = cv2.adaptiveThreshold(imgBlur ,255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV,25,16)

    imgMedian = cv2.medianBlur(imgThreshold,5)
    kernel =np.ones((3,3) , np.uint8)
    imDilate = cv2.dilate(imgMedian ,kernel , iterations=1 )


    checkParkingSpace(imDilate)

    cv2.imshow("Image" , img)
    #cv2.imshow("ImageBlur" ,imgBlur)
    #cv2.imshow("ImageThresh" ,imgThreshold)
    #cv2.imshow("imgMedian", imgMedian)

    cv2.waitKey(7)   # 1 hızlı , 10 daha yavaş