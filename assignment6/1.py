import pyfiglet 
import random
#from termjor import jored
import timeit

def show():
    for i in gameboard:
        for cell in i:
            print(cell, end=" ")
        print()

def check_game():
    x = False
    for i , j in zip(range(0,3), range(0,3)):
            if gameboard[i][0] == gameboard[i][1] == gameboard[i][2] != "_" or gameboard[0][j] == gameboard [1][j] == gameboard[2][j] != "_":
                x = True
    if x or gameboard[0][0] == gameboard[1][1] == gameboard[2][2] != "_" or gameboard[2][0] == gameboard[1][1] == gameboard[0][2] != "_":
        print(winner, "wins!")
        stop = timeit.default_timer()
        print('Time: ', stop - start)
        exit()
    elif not any("_" in i for i in gameboard):
        print("Draw")
        stop = timeit.default_timer()
        print('Time: ', stop - start)
        exit()
    
title = pyfiglet.figlet_format("Tic Tak Toe", font = "slant")

print(title)
print("Welcome to Tic Tac Toe...")
print("For palying with Computer Press 1  ")
print("For Playing with Another Player Press 2 ")
player2_type = int(input())

gameboard = l=[["_" for i in range(3)] for j in range(3)]
show()

while True:
    start = timeit.default_timer()
    print("palyer 1: ")
    
    while True:
        i = int(input("i :"))
        j = int(input("j :"))
        
        if 0 <= i <= 2 and 0 <= j <= 2:
            if gameboard[i][j] == "_":
                gameboard[i][j] = "X"
                break
            else:
                print("This block has been chosen before. Try another one")
        else:
            print("You are just allowed to choose a number between 0 and 2")
    show()
    winner = "player 1"
    check_game()

    if player2_type == 2:
        print("palyer 2: ")
        
        while True:
            i = int(input("i :"))
            j = int(input("j :"))
            
            if 0 <= i <= 2 and 0 <= j <= 2:
                if gameboard[i][j] == "_":        
                    gameboard[i][j] = "O"
                    break
                else: 
                    print("This block has been chosen before. Try another one")
            else:
                print("You are just allowed to choose a number between 0 and 2")

        show()
        winner = "player 2"
        check_game()

    elif player2_type == 1:
        print("player 2: ")
        while True:

            i = random.randint(0 , 2)
            j = random.randint(0 , 2)
            
            if gameboard[i][j] == "_":        
                gameboard[i][j] = jored("O", "blue")
                break

        show()
        winner = "Computer"
        check_game()