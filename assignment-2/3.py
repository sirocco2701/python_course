a=input()
list=[]
while a!="exit":
    list.append(int(a))
    a=input()
print(sum(list)/len(list))