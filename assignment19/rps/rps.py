from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from functools import partial
import random
playerscore=0
computerscore=0
def player (player):
    main_window.player.setText(player)
    db=["rock","paper","scissor"]
    computer=random.choice(db)
    main_window.computer.setText(computer)
    check()

def check():
    global playerscore
    global computerscore
    if (main_window.computer.text()==main_window.player.text()):
        main_window.computer.setText("tie")
    elif ((main_window.computer.text()=="rock" and main_window.player.text()== "scissor")or
          (main_window.computer.text()=="paper"and main_window.player.text()== "rock") or
          (main_window.computer.text()=="scissor" and main_window.player.text()== "paper") ):
        main_window.win.setText("computer wins ")
        computerscore+=1
        main_window.computerscore.setText("computer score: "+str(computerscore))

    else:
        main_window.win.setText("player wins")
        playerscore+=1
        main_window.playerscore.setText("player score: "+str(playerscore))
app = QApplication([])
loader = QUiLoader()
main_window = loader.load("main.ui")
main_window.show()


main_window.rock.clicked.connect(partial(player, "rock"))
main_window.paper.clicked.connect(partial(player, "paper"))
main_window.scissor.clicked.connect(partial(player, "scissor"))

main_window.win.clicked.connect(check)
app.exec()