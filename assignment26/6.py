import cv2
img=cv2.imread("pic2.jpg")

for i in range (img.shape[0]):
    for j in range (img.shape[1]):
        if 150-i==j:
            img[j,i:i+50]=0
            img[i:i+50,j]=0
            
cv2.imshow("",img)
cv2.imwrite("pic6.jpg",img)
cv2.waitKey()