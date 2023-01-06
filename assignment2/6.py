import random
k=input()
while k == "y":
    a=random.randint(1 , 6)
    print(a)

    if a == 6:
        a=random.randint(1 , 6)
        print(a)
        continue
    k=input("y/n")