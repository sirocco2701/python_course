import random
from termcolor import colored
import timeit
import time


def show():
    for i in q:
        for j in i:
            print(j, end=" ")
        print()
    print("**********")

def check_game(lastplayer):
    if (q[0][0]==q[0][1]==q[0][2]!="_" or q[1][0]==q[1][1]==q[1][2]!="_" or q[2][0]==q[2][1]==q[2][2]!="_" or q[0][0]==q[1][0]==q[2][0]!="_" or q[0][1]==q[1][1]==q[2][1]!="_" or q[0][2]==q[1][2]==q[2][2]!="_"  or q[0][0]==q[1][1]==q[2][2]!="_"  or q[0][2]==q[1][1]==q[2][0]!="_"):
        print(lastplayer+"win")
        stop = timeit.default_timer()
        print('Time: ', stop - start)
        exit()
    elif("_" not in str(sum(q, []))):
        print("tie")
        stop = timeit.default_timer()
        print('Time: ', stop - start)
        exit()

def valid(x):
    if x==0 or x==1 or x==2 :
        return 1
    else:
        return 0  

playtype = int(input("Another Player: 1 \nComputer: 2"))
start = timeit.default_timer()
q =[["_" for i in range(3)] for j in range(3)]

show()

if playtype==1:
    lastplayer="o"
    while 1:
        if lastplayer=="o":
            x1,y1=map(int,input().split())
            if valid(x1) and valid(y1)and q[x1][y1]=="_" :
                q[x1][y1]=colored("x", "red")
                show()
                lastplayer="x"
                check_game(lastplayer)
            else:
                print("not available chose again")
                continue
        if lastplayer=="x":
            x2,y2=map(int,input().split())
            if valid(x2) and valid(y2) and q[x2][y2]=="_":
                q[x2][y2]=colored("o", "blue")
                show()
                lastplayer="o"
                check_game(lastplayer)
            elif(lastplayer=="x"):
                print("not available chose again")
                continue
    


else:
    lastplayer="user"
    while 1:
        if lastplayer=="user":
            x2=random.randint(0,2)
            y2=random.randint(0,2)
            if  valid(x2) and valid(y2) and q[x2][y2]=="_" :
                q[x2][y2]=colored("o", "blue")
                time.sleep(2)
                show()
                lastplayer="computer"
                check_game(lastplayer)
            else:
                continue
        if lastplayer=="computer":
            x1,y1=map(int,input().split())
            if  valid(x1) and valid(y1)and q[x1][y1]=="_":
                q[x1][y1]=colored("x", "red")
                show()
                lastplayer="user"
                check_game(lastplayer)
            else:
                print("not available chose again")
            continue
    
print(q)