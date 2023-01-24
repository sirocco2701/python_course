import qrcode

name = input()
phone = input()
QRcode = qrcode.make(name + " " + phone)
QRcode.save("QRCode.png")