# Form implementation generated from reading ui file 'D:\DETAI_BMHTTT\View\ThietKe\signup.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(453, 409)
        MainWindow.setStyleSheet("background-color:rgb(37, 111, 176);\n"
"color:white;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.usernameInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.usernameInput.setGeometry(QtCore.QRect(130, 90, 261, 22))
        self.usernameInput.setStyleSheet("background-color: white;\n"
"border: 2px inset #8b6f78;\n"
"color:black;")
        self.usernameInput.setObjectName("usernameInput")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 81, 16))
        self.label_2.setObjectName("label_2")
        self.passwordInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(130, 139, 201, 22))
        self.passwordInput.setStyleSheet("background-color: white;\n"
"border: 2px inset #8b6f78;\n"
"color:black;")
        self.passwordInput.setInputMask("")
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 10, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 91, 16))
        self.label_3.setObjectName("label_3")
        self.signupButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.signupButton.setGeometry(QtCore.QRect(130, 270, 93, 28))
        self.signupButton.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"border-radius: 10px;\n"
"border: 2px solid black;\n"
"color:black;")
        self.signupButton.setObjectName("signupButton")
        self.cancelButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(250, 270, 93, 28))
        self.cancelButton.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"border-radius: 10px;\n"
"border: 2px solid black;\n"
"color:black;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\DETAI_BMHTTT\\View\\ThietKe\\../Icon/icons8-exit-50.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.cancelButton.setIcon(icon)
        self.cancelButton.setObjectName("cancelButton")
        self.showPasswordButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.showPasswordButton.setGeometry(QtCore.QRect(340, 141, 41, 21))
        self.showPasswordButton.setStyleSheet("background-color: white;\n"
"border: 2px solid black;\n"
"color:black;")
        self.showPasswordButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\DETAI_BMHTTT\\View\\ThietKe\\../Icon/eye.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.showPasswordButton.setIcon(icon1)
        self.showPasswordButton.setObjectName("showPasswordButton")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 196, 91, 16))
        self.label_4.setObjectName("label_4")
        self.passwordInput2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.passwordInput2.setGeometry(QtCore.QRect(130, 195, 201, 22))
        self.passwordInput2.setStyleSheet("background-color: white;\n"
"border: 2px inset #8b6f78;\n"
"color:black;")
        self.passwordInput2.setInputMask("")
        self.passwordInput2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.passwordInput2.setObjectName("passwordInput2")
        self.showPasswordButton2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.showPasswordButton2.setGeometry(QtCore.QRect(340, 197, 41, 21))
        self.showPasswordButton2.setStyleSheet("background-color: white;\n"
"border: 2px solid black;\n"
"color:black;")
        self.showPasswordButton2.setText("")
        self.showPasswordButton2.setIcon(icon1)
        self.showPasswordButton2.setObjectName("showPasswordButton2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 453, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "UserName:"))
        self.label.setText(_translate("MainWindow", "Đăng ký"))
        self.label_3.setText(_translate("MainWindow", "PassWord:"))
        self.signupButton.setText(_translate("MainWindow", "Sign up"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))
        self.label_4.setText(_translate("MainWindow", "PassWord:"))
