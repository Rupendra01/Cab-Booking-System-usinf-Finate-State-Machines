import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

import sqlite3


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("welcomescreen.ui",self)
        qpixmap = QPixmap('welcomescreen.jfif')
        self.label_3.setPixmap(qpixmap)
        self.login.clicked.connect(self.gotologin)
        self.create.clicked.connect(self.gotocreate)

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate(self):
        create = CreateAccScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("login.ui",self)
        qpixmap = QPixmap('login.jpg')
        self.label_5.setPixmap(qpixmap)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.signinfunction)

    def signinfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()

        if len(user)==0 or len(password)==0:
            self.error.setText("Please fill in all inputs.")

        elif user!= 'automata' and password!='utopia':
            self.error.setText("Username or Password is in correct.")
        else:

            # conn = sqlite3.connect("shop_data.db")#cur = conn.cursor()#user_info = [user, password]#cur.execute('INSERT INTO login_info (username, password) VALUES (?,?)', user_info)#conn.commit()#conn.close()
            interface = InterfaceScreen()
            widget.addWidget(interface)
            widget.setCurrentIndex(widget.currentIndex() + 1)


class CreateAccScreen(QDialog):
    def __init__(self):
        super(CreateAccScreen, self).__init__()
        loadUi("createacc.ui",self)
        qpixmap = QPixmap('signup.jpg')
        self.label_6.setPixmap(qpixmap)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpasswordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.signupfunction)

    def signupfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()
        confirmpassword = self.confirmpasswordfield.text()

        if len(user)==0 or len(password)==0 or len(confirmpassword)==0:
            self.error.setText("Please fill in all inputs.")

        elif password!=confirmpassword:
            self.error.setText("Passwords do not match.")
        else:
            conn = sqlite3.connect("shop_data.db")
            cur = conn.cursor()
            user_info = [user, password]
            cur.execute('INSERT INTO login_info (username, password) VALUES (?,?)', user_info)
            conn.commit()
            conn.close()
            interface = InterfaceScreen()
            widget.addWidget(interface)
            widget.setCurrentIndex(widget.currentIndex()+1)

class InterfaceScreen(QDialog):
    def __init__(self):
        super(InterfaceScreen, self).__init__()
        loadUi("interface.ui",self)
        qpixmap = QPixmap('main screen.jpg')
        self.label_2.setPixmap(qpixmap)
        self.book.clicked.connect(self.preparingfunction)

    def preparingfunction(self):
        prepare = PreparingScreen()
        widget.addWidget(prepare)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class PreparingScreen(QDialog):
    def __init__(self):
        super(PreparingScreen, self).__init__()
        loadUi("preparing.ui",self)
        qpixmap = QPixmap('ride.jpg')
        self.prep.setPixmap(qpixmap)
        self.information.clicked.connect(self.informationfunction)
        self.process.clicked.connect(self.processfunction)
        self.cancel.clicked.connect(self.cancelfunction)
        self.otp.clicked.connect(self.otpfunction)

    def informationfunction(self):
        interface = InterfaceScreen1()
        widget.addWidget(interface)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def processfunction(self):
        interface = InterfaceScreen2()
        widget.addWidget(interface)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def cancelfunction(self):
        interface = InterfaceScreen3()
        widget.addWidget(interface)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def otpfunction(self):
        interface = InterfaceScreen4()
        widget.addWidget(interface)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class InterfaceScreen1(QDialog):
    def __init__(self):
        super(InterfaceScreen1, self).__init__()
        loadUi("information.ui",self)
        qpixmap = QPixmap('information.jpg')
        self.inf.setPixmap(qpixmap)
        self.mainmenu.clicked.connect(self.informationfunction)

    def informationfunction(self):
        interface = InterfaceScreen()
        widget.addWidget(interface)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class InterfaceScreen2(QDialog):
    def __init__(self):
        super(InterfaceScreen2, self).__init__()
        loadUi("processing.ui",self)
        qpixmap = QPixmap('processing.jfif')
        self.pros.setPixmap(qpixmap)
        self.req.clicked.connect(self.requestfunction)
        self.una.clicked.connect(self.unavailablefunction)
        self.exp.clicked.connect(self.expirefunction)
        self.can.clicked.connect(self.cancelfunction)

    def requestfunction(self):
        interface = InterfaceScreen5()
        widget.addWidget(interface)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def unavailablefunction(self):
        interface = InterfaceScreen3()
        widget.addWidget(interface)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def expirefunction(self):
        interface = InterfaceScreen3()
        widget.addWidget(interface)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def cancelfunction(self):
        interface = InterfaceScreen3()
        widget.addWidget(interface)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class InterfaceScreen3(QDialog):
    def __init__(self):
        super(InterfaceScreen3, self).__init__()
        loadUi("cancel.ui",self)
        qpixmap = QPixmap('cancel.jpg')
        self.can.setPixmap(qpixmap)
        self.click.clicked.connect(self.informationfunction)

    def informationfunction(self):
        interface = InterfaceScreen()
        widget.addWidget(interface)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class InterfaceScreen4(QDialog):
    def __init__(self):
        super(InterfaceScreen4, self).__init__()
        loadUi("otp.ui",self)
        qpixmap = QPixmap('welcomescreen.jfif')
        widget.setFixedHeight(306)
        widget.setFixedWidth(431)
        self.ot.setPixmap(qpixmap)
        self.otp.clicked.connect(self.otpfunction)

    def otpfunction(self):
        interface = InterfaceScreen6()
        widget.addWidget(interface)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class InterfaceScreen5(QDialog):
    def __init__(self):
        super(InterfaceScreen5, self).__init__()
        loadUi("requesting.ui",self)
        qpixmap = QPixmap('requesting.png')
        self.req.setPixmap(qpixmap)
        widget.setFixedHeight(841)
        widget.setFixedWidth(1201)
        self.acc.clicked.connect(self.acceptfunction)
        self.rej.clicked.connect(self.rejectfunction)
        self.tim.clicked.connect(self.timeoutfunction)
        self.can.clicked.connect(self.cancelfunction)

    def acceptfunction(self):
        interface = InterfaceScreen6()
        widget.addWidget(interface)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def rejectfunction(self):
        interface = InterfaceScreen3()
        widget.addWidget(interface)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def timeoutfunction(self):
        interface = InterfaceScreen3()
        widget.addWidget(interface)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def cancelfunction(self):
        interface = InterfaceScreen3()
        widget.addWidget(interface)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class InterfaceScreen6(QDialog):
    def __init__(self):
        super(InterfaceScreen6, self).__init__()
        loadUi("inprogess.ui",self)
        widget.setFixedHeight(800)
        widget.setFixedWidth(1200)
        qpixmap = QPixmap('inprogess.jfif')
        self.inp.setPixmap(qpixmap)
        self.fin.clicked.connect(self.finishfunction)

    def finishfunction(self):
        interface = InterfaceScreen7()
        widget.addWidget(interface)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class InterfaceScreen7(QDialog):
    def __init__(self):
        super(InterfaceScreen7, self).__init__()
        loadUi("finished.ui",self)
        qpixmap = QPixmap('finished.jpg')
        widget.setFixedHeight(873)
        widget.setFixedWidth(1271)
        self.fin.setPixmap(qpixmap)
        self.han.clicked.connect(self.handoverfunction)
        self.pay.clicked.connect(self.payonlinefunction)

    def handoverfunction(self):
        interface = InterfaceScreen8()
        widget.addWidget(interface)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def payonlinefunction(self):
        interface = InterfaceScreen8()
        widget.addWidget(interface)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class InterfaceScreen8(QDialog):
    def __init__(self):
        super(InterfaceScreen8, self).__init__()
        loadUi("completed.ui",self)
        qpixmap = QPixmap('completed.jpg')
        self.com.setPixmap(qpixmap)
        qpixmap = QPixmap('completed1.jpg')
        self.com1.setPixmap(qpixmap)
        self.skip.clicked.connect(self.skipfunction)
        self.rate.clicked.connect(self.rateusfunction)

    def skipfunction(self):
        interface = InterfaceScreen()
        widget.addWidget(interface)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def rateusfunction(self):
        interface = InterfaceScreen()
        widget.addWidget(interface)
        widget.setCurrentIndex(widget.currentIndex() + 1)
# main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")