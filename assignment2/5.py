a=int(input())
h=a//3600
a%=3600
m=a//60
s=a%60
print("%.2d"%h+":"+"%.2d"%m+":"+"%.2d"%s)