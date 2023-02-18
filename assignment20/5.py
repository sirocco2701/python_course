a=[1,2,2,1]
d=0
for i in range(len(a)//2):
    if a[i]==a[len(a)-i-1]:
        d+=1
if d==len(a)//2:
    print("yes")
else:
    print("no")