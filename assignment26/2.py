import cv2
img=cv2.imread("img2.webp")

for i in range (img.shape[0]):
    for j in range (img.shape[1]):
        img[i,j]=(255-img[i,j])
        
cv2.imshow("",img)
cv2.imwrite("pic2.jpg",img)
cv2.waitKey()