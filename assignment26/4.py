import cv2
import numpy
x=int(input("inter the size"))
img=numpy.zeros((x,x))
#img=cv2.imread("1.jpg")    #or import a black image
img[x//10:x//10*9,x//4:x//4+x//20]=255
img[x//10:x//10*9,x-(x//4)-x//20:x-(x//4)]=255
img[x//2-x//40:x//2+x//40,x//4:x-(x//4)-x//20]=255

cv2.imshow("",img)
cv2.imwrite("name.jpg",img)
cv2.waitKey()