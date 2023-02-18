import random
c1=0
c2=0
c3=0

for i in range(5):

    a=int(input())
    p1=random.randint(1,2)
    p2=random.randint(1,2)
    print("computer1",p1,"computer2",p2)
    if p1==p2==a:
        pass
    elif p1==p2:
        c1+=1
    elif p1==a:
        c3+=1
    elif p2==a:
        c2+=1
    print("scores: ","player:",c1,"computer:",c2,"computer2:",c3)


