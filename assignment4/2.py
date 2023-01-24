import math
a=int(input())
j=1
l=[0]
while a>max(l):
    l.append(math.factorial(j))
    if a in l:
        j=1
        break
    j+=1 
if j!=1:
    print("no")