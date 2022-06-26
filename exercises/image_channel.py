import cv2
import matplotlib.pyplot as plt

img = cv2.imread("shape.jpg")
plt.imshow(img)
plt.show()

"""
rgb
[50,50,1]
[50,50,0]
"""
r=img[:,:,0]
g=img[:,:,1]
b=img[:,:,2]

output = [img,r,g,b]
titles = ["image","r","g","b"]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.axis("off")
    plt.title(titles[i])
    if i ==0:
        plt.imshow(output[i])
    else:
        plt.imshow(output[i],cmap="gray")
    plt.show()