from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
import random
import time
endgame=False
xscore=0
yscore=0
tiescore=0
gamemode=0
odd=0
winer=""

def setmood(mood):
    global gamemode
    if mood==0:
        gamemode=0
    else:
        gamemode=1

def newgame():
    global player
    global endgame
    global odd
    for i in range(3):
            for j in range(3):
                buttons[i][j].setText("")
                buttons[i][j].setStyleSheet("background-color:rgba( 63, 63, 63 ,0.7);")
    for i in range(3):
            for j in range(3):
                buttons[i][j].setEnabled(True)
    endgame=False
    odd+=1
    if odd%2==1 and gamemode==1:
                    row=random.randint(0,2)
                    col=random.randint(0,2)
                    buttons[row][col].setText("O")
                    buttons[row][col].setStyleSheet("color :  rgb(2, 32, 62); background-color : rgb( 21, 87, 153 );")
                    player = 1
                    main_window.turn.setText("X turn")
                    main_window.turn.setStyleSheet("color :  rgb(2, 32, 62); background-color : rgb( 78, 225, 116 );")


def isempty():
    z=0
    for i in range(3):
        for j in range(3):
            if buttons[i][j].text()=="":
                z=1
    if z==1:
        return True
    
def check():
    global player
    global endgame
    global winer
    winer="tie"
    if ((buttons[0][0].text() == buttons[0][1].text() == buttons[0][2].text() and buttons[0][0].text()!="") or
        (buttons[1][0].text() == buttons[1][1].text() == buttons[1][2].text() and buttons[1][0].text()!="") or
        (buttons[2][0].text() == buttons[2][1].text() == buttons[2][2].text() and buttons[2][0].text()!="") or
        (buttons[0][0].text() == buttons[1][0].text() == buttons[2][0].text() and buttons[0][0].text()!="") or
        (buttons[0][1].text() == buttons[1][1].text() == buttons[2][1].text() and buttons[0][1].text()!="") or
        (buttons[0][2].text() == buttons[1][2].text() == buttons[2][2].text() and buttons[0][2].text()!="") or
        (buttons[0][0].text() == buttons[1][1].text() == buttons[2][2].text() and buttons[0][0].text()!="") or
        (buttons[0][2].text() == buttons[1][1].text() == buttons[2][0].text() and buttons[0][2].text()!="")) :
        if player==1:
            winer="O"
        else:
            winer="X"
        msg_box = QMessageBox(text = "Player "+winer+" wins!")
        endgame=True
        msg_box.exec()
    else:
        if not isempty():
            msg_box = QMessageBox(text = "tie")
            endgame=True
            msg_box.exec() 

def play(row, col):
    global player
    global buttons
    global endgame
    global winer
    global firstround
    global xscore
    global yscore
    global tiescore

    if gamemode==0:
        if player == 1:
            if buttons[row][col].text()=='':
                buttons[row][col].setText("X")
                buttons[row][col].setStyleSheet("color : rgb( 1, 93, 24 ); background-color : rgb(  78, 225, 116 );")
                player = 2
                main_window.turn.setText("O turn")
                main_window.turn.setStyleSheet("color :  rgb(2, 32, 62); background-color : rgb( 21, 87, 153 );")
        
        elif player == 2:
            if buttons[row][col].text()=='':
                buttons[row][col].setText("O")
                buttons[row][col].setStyleSheet("color :  rgb(2, 32, 62); background-color : rgb( 21, 87, 153 );")
                player = 1
                main_window.turn.setText("X turn")
                main_window.turn.setStyleSheet("color :  rgb(2, 32, 62); background-color : rgb( 78, 225, 116 );")
        check()
    else:
            if buttons[row][col].text()=='':
                buttons[row][col].setText("X")
                buttons[row][col].setStyleSheet("color : rgb( 1, 93, 24 ); background-color : rgb(  78, 225, 116);")
                player = 2
                firstround=False
                #time.sleep(2)
                main_window.turn.setText("O turn")
                main_window.turn.setStyleSheet("color :  rgb(2, 32, 62); background-color : rgb( 21, 87, 153 );")
            check()    
            c=0
            print(winer)
            if isempty() and winer!='X' : 
                
                while c==0 :
                    row=random.randint(0,2)
                    col=random.randint(0,2)
                    if buttons[row][col].text()=='':
                        buttons[row][col].setText("O")
                        buttons[row][col].setStyleSheet("color :  rgb(2, 32, 62); background-color : rgb( 21, 87, 153 );")
                        player = 1
                        main_window.turn.setText("X turn")
                        main_window.turn.setStyleSheet("color :  rgb(2, 32, 62); background-color : rgb( 78, 225, 116 );")
                        c=1
                        check()

    if endgame:
        for i in range(3):
            for j in range(3):
                buttons[i][j].setEnabled(False)
        if winer=="X":
            xscore+=1
            main_window.scorex.setText("x score: "+str(xscore))
        elif winer=="O":
            yscore+=1
            main_window.scorey.setText("y score: "+str(yscore))
        else:
            tiescore+=1
            main_window.scoretie.setText("tie score: "+str(tiescore))

app = QApplication([])

player = 1 

loader = QUiLoader()
main_window = loader.load("main.ui")
main_window.show()

buttons = [[main_window.btn_1, main_window.btn_2, main_window.btn_3],
           [main_window.btn_4, main_window.btn_5, main_window.btn_6],
           [main_window.btn_7, main_window.btn_8, main_window.btn_9]] 

for i in range(3):
    for j in range (3):
        buttons[i][j].clicked.connect(partial(play, i , j))

main_window.computer.clicked.connect(partial(setmood,1))
main_window.player.clicked.connect(partial(setmood,0))
main_window.newgame.clicked.connect(newgame)
app.exec()