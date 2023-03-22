import cv2
img=cv2.imread("3.webp")
img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img2.shape)
w,h=img2.shape

for i in range ((w//2)+1):
    for j in range (h):
        temp=img2[i,j]
        img2[i,j]=img2[w-i-1,h-j-1]
        img2[w-i-1,h-j-1]=temp
        if (i==w//2 and j==h//2):
            break
cv2.imshow("",img2)
cv2.imwrite("pic3.jpg",img2)
cv2.waitKey()