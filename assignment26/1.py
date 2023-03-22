import cv2
import numpy

length=int(input())
hight=int(input())
size=int(input())
img=numpy.zeros((length,hight))
#img=cv2.imread("1.jpg")    #or import a black image

for i in range (0,img.shape[0]):
    for j in range (0,img.shape[1],2):
       img[i*size:(i+1)*size,(j+(i%2))*size:(j+(i%2)+1)*size]=255 

cv2.imshow("",img)
cv2.imwrite("chessboard.jpg",img)
cv2.waitKey()