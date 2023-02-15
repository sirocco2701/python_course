from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from functools import partial
import random
m=''
def gen():
    if(m=="n") :
        charr=chr(random.randint(33,47))
        num=chr(random.randint(48,57))
        lett=chr(random.randint(97,126))
        clett=chr(random.randint(65,90))
        password=charr+num+lett+clett
        for i in range (4):
            password+=chr(random.randint(33,126))
        

    else:
        char1=chr(random.randint(33,47))
        char2=chr(random.randint(33,47))
        num1=chr(random.randint(48,57))
        num2=chr(random.randint(48,57))
        lett1=chr(random.randint(97,126))
        lett2=chr(random.randint(97,126))
        clett1=chr(random.randint(65,90))
        clett2=chr(random.randint(65,90))
        password=char1+num1+lett1+clett1+char2+num2+lett2+clett2
    
        for i in range (4):
             password+=chr(random.randint(33,126))
    main_window.passbox.setText(''.join(random.sample(password,len(password))))
def setmode(mode):
    global m
    if mode=="normal":
        m="n"
    else:
        m="s"
app = QApplication([])
loader = QUiLoader()
main_window = loader.load("main.ui")
main_window.show()


main_window.gen.clicked.connect(gen)
main_window.normalpass.clicked.connect(partial(setmode,"normal"))
main_window.superpass.clicked.connect(partial(setmode,"supe"))

app.exec()