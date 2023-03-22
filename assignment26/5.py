import cv2
img=cv2.imread("1.jpg")    #or import a black image
h=img.shape[0]
for i in range (0,h):
    img[i,:]=(255-i)
cv2.imshow("",img)
cv2.imwrite("gradient.jpg",img)
cv2.waitKey()