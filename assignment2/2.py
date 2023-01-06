import random

user_score = 0
computer_score = 0
r = 0

while user_score != 5 and computer_score != 5:
   
    x = random.randint(1, 3)

    y= int(input("r=1,p=2,s=3 inter num") )

    if y>3:
        print("not valid")
        continue

    if ((x == 1 and y == 2)or (x== 2 and y == 3) or(x==3 and y==1)):
        user_score += 1

    elif ((x == 1 and y == 3)or(x== 2 and y== 1)or (x==3 and y==2)):
        computer_score += 1

    elif x==y:
        print("try again")    
    
    r = r + 1 
    print("computer's choice is :" , x)
    print("You :", user_score , "computer :" , computer_score)  



if user_score > computer_score:
    print("You won after", r , "attempts")
            #break
else:
    print("Sorry! computer won after" , r , "attempts")
            #break
