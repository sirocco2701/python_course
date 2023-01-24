from random import randint as rnd

computer = rnd(1, 100)

for i in range(10):
    user = int(input())

    if computer == user:
        print("You win" , i+1 )
        break

    elif computer > user:
        print("go up ")

    elif computer < user:
        print("go down ")   