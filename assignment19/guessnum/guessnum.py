from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from functools import partial
import random
begining=0
a=0
b=0
z=''
l=[]
def check():
    global a
    global b
    global z
    global begining
    global w
    global l
    if begining==0:
        m,n=main_window.guess.text().split()
        a=int(m)
        b=int(n)
        g=int((a+b)/2)
        w=random.randint(g-(int(g*0.1)),g+(int(g*0.1)))
        print(w)
        main_window.check.setText("is "+str(w)+" your number?")
        begining=1
    else:
        print(a,b)
        print(z)
        w=random.randint(a,b)
        print(w)
        while w in l:
            w=random.randint(a,b)
        l.append(w)
        main_window.check.setText("is "+str(w)+" your number?")
        if z=="r":
            print("end")
            main_window.check.setText("yeyyyyy i did it do you wanna play again? intr your nmber")
            main_window.guess.setText("")
            begining=0

def status(s):
    global z
    global a
    global b
    global w
    if s=="h":
        z= "h"
        a=w
        check()
    elif s=="l":
       z= "l"
       b=w
       check()
    elif s=="r":
       z="r"
       check()

app = QApplication([])
loader = QUiLoader()
main_window = loader.load("main.ui")
main_window.show()


main_window.check.clicked.connect(check)
main_window.higher.clicked.connect(partial(status,"h"))
main_window.low.clicked.connect(partial(status,"l"))
main_window.right.clicked.connect(partial(status,"r"))

app.exec()