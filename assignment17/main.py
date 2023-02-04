from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from functools import partial
import math

re=['0',"+"]
def sub():
    global re
    a = (main_window.txt_box.text())
    if a=="":
        re= re[:len(re)-1]
        if '' in re:
            re.remove('')

    re.append(a)
    re.append("-")
    main_window.txt_box_2.setText(show(re))
    main_window.txt_box.setText("")

def sum():
    global re
    a = (main_window.txt_box.text())
    if a=="":
        re= re[:len(re)-1]
        if '' in re:
            re.remove('')
    re.append(a)
    re.append("+")
    main_window.txt_box_2.setText(show(re))
    main_window.txt_box.setText("")

def mul():
    global re
    a = (main_window.txt_box.text())
    if a=="":
        re= re[:len(re)-1]
        if '' in re:
            re.remove('')
    re.append(a)
    re.append("*")
    main_window.txt_box_2.setText(show(re))
    main_window.txt_box.setText("")

def div():
    global re
    a = (main_window.txt_box.text())
    if a=="":
        re= re[:len(re)-1]
        if '' in re:
            re.remove('')
    re.append(a)
    re.append("/")
    main_window.txt_box_2.setText(show(re))
    main_window.txt_box.setText("")

def sin():
    global re
    a = (main_window.txt_box.text())
    main_window.txt_box_2.setText(show(re))
    main_window.txt_box.setText(str(math.sin(math.radians(float(a)))))

def cos():
    global re
    a = (main_window.txt_box.text())
    main_window.txt_box_2.setText(show(re))
    main_window.txt_box.setText(str(math.cos(math.radians(float(a)))))

def tan():
    global re
    a = (main_window.txt_box.text())
    main_window.txt_box_2.setText(show(re))
    main_window.txt_box.setText(str(math.tan(math.radians(float(a)))))

def cot():
    global re
    a = (main_window.txt_box.text())
    main_window.txt_box_2.setText(show(re))
    main_window.txt_box.setText(str(1/math.tan(math.radians(float(a)))))

def log():
    global re
    a = (main_window.txt_box.text())
    main_window.txt_box_2.setText(show(re))
    main_window.txt_box.setText(str(math.log(float(a))))

def sqrt():
    global re
    a = (main_window.txt_box.text())
    main_window.txt_box_2.setText(show(re))
    main_window.txt_box.setText(str(math.log(float(a))))

def sign():
    global re
    a = (main_window.txt_box.text())
    main_window.txt_box_2.setText(show(re))
    main_window.txt_box.setText(str(-1*(float(a))))

def pers():
    global re
    a = (main_window.txt_box.text())
    main_window.txt_box_2.setText(show(re))
    main_window.txt_box.setText(str((float(a))/100))


def result():
    global c
    global re
    c = (main_window.txt_box.text())
    if c=='':
        re= re[:len(re)-1]
        print(1)
        if '' in re:
            re.remove('')
            print(2)
    re.append(c)
    re.append("=")
    final=calculate(re)
    main_window.txt_box_2.setText(show(re))
    main_window.txt_box.setText(str(final))  

def clr():
    global re
    if main_window.txt_box.text()=='':
        re= re[:len(re)-1]
        if '' in re:
            re.remove('')
        main_window.txt_box.setText(re[-1])
        re= re[:len(re)-1]
        if '' in re:
            re.remove('')
    else:
        main_window.txt_box.setText(main_window.txt_box.text()[:len(main_window.txt_box.text())-1])
    main_window.txt_box_2.setText(show(re))

def allclr():
    global re
    main_window.txt_box_2.setText("")
    main_window.txt_box.setText("")
    re=["0","+"]

def calculate(re):
    print(len(re))
    print(re)
    res=float(re[0])
    for i in range(1,len(re)):
        if re[i]=="-":
            res-=float(re[i+1])
        elif(re[i]=="+"):
            res+=float(re[i+1])
        elif(re[i]=="*"):
            res*=float(re[i+1])
        elif(re[i]=="/"):
            res/=float(re[i+1])
    return res

def show(re):
    w=''
    for i in range(2,len(re)):
        w+=re[i]+" "
        if re[i]=='=':
            w=''
    return w

app = QApplication([])
loader = QUiLoader()
main_window = loader.load("main.ui")
main_window.show()

def num(number):
    main_window.txt_box.setText(main_window.txt_box.text()+number)

def dec():
    if '.' not in main_window.txt_box.text():
        if main_window.txt_box.text()!='':
            main_window.txt_box.setText(main_window.txt_box.text()+'.')
        else:
            main_window.txt_box.setText('0.')

main_window.sum.clicked.connect(sum)
main_window.sub.clicked.connect(sub)
main_window.mul.clicked.connect(mul)
main_window.div.clicked.connect(div)
main_window.sin.clicked.connect(sin)
main_window.cos.clicked.connect(cos)
main_window.tan.clicked.connect(tan)
main_window.cot.clicked.connect(cot)
main_window.log.clicked.connect(log)
main_window.sqrt.clicked.connect(sqrt)
main_window.sign.clicked.connect(sign)
main_window.pers.clicked.connect(pers)
main_window.clr.clicked.connect(clr)
main_window.allclr.clicked.connect(allclr)
main_window.equal.clicked.connect(result)
main_window.num1.clicked.connect(partial(num, "1"))
main_window.num2.clicked.connect(partial(num, "2"))
main_window.num3.clicked.connect(partial(num, "3"))
main_window.num4.clicked.connect(partial(num, "4"))
main_window.num5.clicked.connect(partial(num, "5"))
main_window.num6.clicked.connect(partial(num, "6"))
main_window.num7.clicked.connect(partial(num, "7"))
main_window.num8.clicked.connect(partial(num, "8"))
main_window.num9.clicked.connect(partial(num, "9"))
main_window.num0.clicked.connect(partial(num, "0"))
main_window.dec.clicked.connect(dec)

app.exec()