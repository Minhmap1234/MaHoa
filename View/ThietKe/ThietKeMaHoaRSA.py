# Form implementation generated from reading ui file 'D:\DETAI_BMHTTT\View\ThietKe\ThietKeMaHoaRSA.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(944, 646)
        Dialog.setStyleSheet("background-color:rgb(37, 111, 176);\n"
"color:white;")
        self.btnSaveFile = QtWidgets.QPushButton(parent=Dialog)
        self.btnSaveFile.setGeometry(QtCore.QRect(700, 600, 93, 28))
        self.btnSaveFile.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"border-radius: 10px;\n"
"border: 2px solid black;\n"
"color:black;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\DETAI_BMHTTT\\View\\ThietKe\\../Icon/icons8-save-file-64.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnSaveFile.setIcon(icon)
        self.btnSaveFile.setObjectName("btnSaveFile")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(290, 360, 181, 16))
        self.label_4.setObjectName("label_4")
        self.btnOpenFile = QtWidgets.QPushButton(parent=Dialog)
        self.btnOpenFile.setGeometry(QtCore.QRect(700, 340, 93, 28))
        self.btnOpenFile.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"border-radius: 10px;\n"
"border: 2px solid black;\n"
"color:black;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\DETAI_BMHTTT\\View\\ThietKe\\../Icon/icons8-open-file-40.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnOpenFile.setIcon(icon1)
        self.btnOpenFile.setObjectName("btnOpenFile")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(290, 80, 181, 16))
        self.label_2.setObjectName("label_2")
        self.btnMaHoa = QtWidgets.QPushButton(parent=Dialog)
        self.btnMaHoa.setGeometry(QtCore.QRect(820, 340, 93, 28))
        self.btnMaHoa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"border-radius: 10px;\n"
"border: 2px solid black;\n"
"color:black;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:\\DETAI_BMHTTT\\View\\ThietKe\\../Icon/icons8-encode-32.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnMaHoa.setIcon(icon2)
        self.btnMaHoa.setObjectName("btnMaHoa")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(600, 10, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtCiphertext = QtWidgets.QTextEdit(parent=Dialog)
        self.txtCiphertext.setGeometry(QtCore.QRect(290, 380, 621, 211))
        self.txtCiphertext.setStyleSheet("background-color: white;\n"
"border: 2px inset #8b6f78;\n"
"border-radius:20px;\n"
"color:black;")
        self.txtCiphertext.setObjectName("txtCiphertext")
        self.txtPlaintext = QtWidgets.QTextEdit(parent=Dialog)
        self.txtPlaintext.setGeometry(QtCore.QRect(290, 110, 621, 221))
        self.txtPlaintext.setStyleSheet("background-color: white;\n"
"border: 2px inset #8b6f78;\n"
"border-radius:20px;\n"
"color:black;")
        self.txtPlaintext.setObjectName("txtPlaintext")
        self.btnClose = QtWidgets.QPushButton(parent=Dialog)
        self.btnClose.setGeometry(QtCore.QRect(820, 600, 93, 28))
        self.btnClose.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"border-radius: 10px;\n"
"border: 2px solid black;\n"
"color:black;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("D:\\DETAI_BMHTTT\\View\\ThietKe\\../Icon/icons8-exit-50.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnClose.setIcon(icon3)
        self.btnClose.setObjectName("btnClose")
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 10, 228, 581))
        self.frame.setStyleSheet("QFrame {\n"
"  border-width: 1px;\n"
"  border: 1px inset #8b6f78;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.toolBox = QtWidgets.QToolBox(parent=self.frame)
        self.toolBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.toolBox.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.toolBox.setStyleSheet("QPushButton {\n"
"  background-color: #FFC4D0;\n"
"}\n"
"QToolBox {\n"
" background-color: #FFFFFF;;\n"
"  color: #EEEEEE;\n"
"}")
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 196, 387))
        self.page.setObjectName("page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_6 = QtWidgets.QFrame(parent=self.page)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.actionHai_dong_MaHoa = QtWidgets.QPushButton(parent=self.frame_6)
        self.actionHai_dong_MaHoa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionHai_dong_MaHoa.setObjectName("actionHai_dong_MaHoa")
        self.verticalLayout_5.addWidget(self.actionHai_dong_MaHoa)
        self.actionNhieu_dong_MaHoa = QtWidgets.QPushButton(parent=self.frame_6)
        self.actionNhieu_dong_MaHoa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionNhieu_dong_MaHoa.setObjectName("actionNhieu_dong_MaHoa")
        self.verticalLayout_5.addWidget(self.actionNhieu_dong_MaHoa)
        self.verticalLayout_3.addWidget(self.frame_6, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 196, 387))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_10 = QtWidgets.QFrame(parent=self.page_2)
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.actionCeasar_MaHoa = QtWidgets.QPushButton(parent=self.frame_10)
        self.actionCeasar_MaHoa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionCeasar_MaHoa.setObjectName("actionCeasar_MaHoa")
        self.verticalLayout_6.addWidget(self.actionCeasar_MaHoa)
        self.actionVignere_MaHoa = QtWidgets.QPushButton(parent=self.frame_10)
        self.actionVignere_MaHoa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionVignere_MaHoa.setObjectName("actionVignere_MaHoa")
        self.verticalLayout_6.addWidget(self.actionVignere_MaHoa)
        self.actionBelasco_MaHoa = QtWidgets.QPushButton(parent=self.frame_10)
        self.actionBelasco_MaHoa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionBelasco_MaHoa.setObjectName("actionBelasco_MaHoa")
        self.verticalLayout_6.addWidget(self.actionBelasco_MaHoa)
        self.actionTrithemius_MaHoa = QtWidgets.QPushButton(parent=self.frame_10)
        self.actionTrithemius_MaHoa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionTrithemius_MaHoa.setObjectName("actionTrithemius_MaHoa")
        self.verticalLayout_6.addWidget(self.actionTrithemius_MaHoa)
        self.verticalLayout_4.addWidget(self.frame_10, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 196, 387))
        self.page_3.setObjectName("page_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_11 = QtWidgets.QFrame(parent=self.page_3)
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.actionXORCeasar_MaHoa = QtWidgets.QPushButton(parent=self.frame_11)
        self.actionXORCeasar_MaHoa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionXORCeasar_MaHoa.setObjectName("actionXORCeasar_MaHoa")
        self.verticalLayout_9.addWidget(self.actionXORCeasar_MaHoa)
        self.actionXORVignere_MaHoa = QtWidgets.QPushButton(parent=self.frame_11)
        self.actionXORVignere_MaHoa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionXORVignere_MaHoa.setObjectName("actionXORVignere_MaHoa")
        self.verticalLayout_9.addWidget(self.actionXORVignere_MaHoa)
        self.actionXORBelasco_MaHoa = QtWidgets.QPushButton(parent=self.frame_11)
        self.actionXORBelasco_MaHoa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionXORBelasco_MaHoa.setObjectName("actionXORBelasco_MaHoa")
        self.verticalLayout_9.addWidget(self.actionXORBelasco_MaHoa)
        self.actionXORTrithemius_MaHoa = QtWidgets.QPushButton(parent=self.frame_11)
        self.actionXORTrithemius_MaHoa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionXORTrithemius_MaHoa.setObjectName("actionXORTrithemius_MaHoa")
        self.verticalLayout_9.addWidget(self.actionXORTrithemius_MaHoa)
        self.verticalLayout_7.addWidget(self.frame_11, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 196, 387))
        self.page_4.setObjectName("page_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_12 = QtWidgets.QFrame(parent=self.page_4)
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.actionDES_MaHoa = QtWidgets.QPushButton(parent=self.frame_12)
        self.actionDES_MaHoa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionDES_MaHoa.setObjectName("actionDES_MaHoa")
        self.verticalLayout_10.addWidget(self.actionDES_MaHoa)
        self.actionAES_MaHoa = QtWidgets.QPushButton(parent=self.frame_12)
        self.actionAES_MaHoa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionAES_MaHoa.setObjectName("actionAES_MaHoa")
        self.verticalLayout_10.addWidget(self.actionAES_MaHoa)
        self.actionRSA_MaHoa = QtWidgets.QPushButton(parent=self.frame_12)
        self.actionRSA_MaHoa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionRSA_MaHoa.setObjectName("actionRSA_MaHoa")
        self.verticalLayout_10.addWidget(self.actionRSA_MaHoa)
        self.verticalLayout_11.addWidget(self.frame_12, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.toolBox.addItem(self.page_4, "")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 196, 387))
        self.page_5.setObjectName("page_5")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.frame_13 = QtWidgets.QFrame(parent=self.page_5)
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_19.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.actionHai_dong_GiaiMa = QtWidgets.QPushButton(parent=self.frame_13)
        self.actionHai_dong_GiaiMa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionHai_dong_GiaiMa.setObjectName("actionHai_dong_GiaiMa")
        self.verticalLayout_19.addWidget(self.actionHai_dong_GiaiMa)
        self.actionNhieu_dong_GiaiMa = QtWidgets.QPushButton(parent=self.frame_13)
        self.actionNhieu_dong_GiaiMa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionNhieu_dong_GiaiMa.setObjectName("actionNhieu_dong_GiaiMa")
        self.verticalLayout_19.addWidget(self.actionNhieu_dong_GiaiMa)
        self.verticalLayout_18.addWidget(self.frame_13, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.toolBox.addItem(self.page_5, "")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setGeometry(QtCore.QRect(0, 0, 196, 387))
        self.page_6.setObjectName("page_6")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.page_6)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.frame_18 = QtWidgets.QFrame(parent=self.page_6)
        self.frame_18.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_21.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.actionCeasar_GiaiMa = QtWidgets.QPushButton(parent=self.frame_18)
        self.actionCeasar_GiaiMa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionCeasar_GiaiMa.setObjectName("actionCeasar_GiaiMa")
        self.verticalLayout_21.addWidget(self.actionCeasar_GiaiMa)
        self.actionVignere_GiaiMa = QtWidgets.QPushButton(parent=self.frame_18)
        self.actionVignere_GiaiMa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionVignere_GiaiMa.setObjectName("actionVignere_GiaiMa")
        self.verticalLayout_21.addWidget(self.actionVignere_GiaiMa)
        self.actionBelasco_GiaiMa = QtWidgets.QPushButton(parent=self.frame_18)
        self.actionBelasco_GiaiMa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionBelasco_GiaiMa.setObjectName("actionBelasco_GiaiMa")
        self.verticalLayout_21.addWidget(self.actionBelasco_GiaiMa)
        self.actionTrithemius_GiaiMa = QtWidgets.QPushButton(parent=self.frame_18)
        self.actionTrithemius_GiaiMa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionTrithemius_GiaiMa.setObjectName("actionTrithemius_GiaiMa")
        self.verticalLayout_21.addWidget(self.actionTrithemius_GiaiMa)
        self.verticalLayout_20.addWidget(self.frame_18, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.toolBox.addItem(self.page_6, "")
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setGeometry(QtCore.QRect(0, 0, 196, 387))
        self.page_7.setObjectName("page_7")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.page_7)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.frame_19 = QtWidgets.QFrame(parent=self.page_7)
        self.frame_19.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_23.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.actionXORCeasar_GiaiMa = QtWidgets.QPushButton(parent=self.frame_19)
        self.actionXORCeasar_GiaiMa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionXORCeasar_GiaiMa.setObjectName("actionXORCeasar_GiaiMa")
        self.verticalLayout_23.addWidget(self.actionXORCeasar_GiaiMa)
        self.actionXORVignere_GiaiMa = QtWidgets.QPushButton(parent=self.frame_19)
        self.actionXORVignere_GiaiMa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionXORVignere_GiaiMa.setObjectName("actionXORVignere_GiaiMa")
        self.verticalLayout_23.addWidget(self.actionXORVignere_GiaiMa)
        self.actionXORBelasco_GiaiMa = QtWidgets.QPushButton(parent=self.frame_19)
        self.actionXORBelasco_GiaiMa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionXORBelasco_GiaiMa.setObjectName("actionXORBelasco_GiaiMa")
        self.verticalLayout_23.addWidget(self.actionXORBelasco_GiaiMa)
        self.actionXORTrithemius_GiaiMa = QtWidgets.QPushButton(parent=self.frame_19)
        self.actionXORTrithemius_GiaiMa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionXORTrithemius_GiaiMa.setObjectName("actionXORTrithemius_GiaiMa")
        self.verticalLayout_23.addWidget(self.actionXORTrithemius_GiaiMa)
        self.verticalLayout_22.addWidget(self.frame_19, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.toolBox.addItem(self.page_7, "")
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setGeometry(QtCore.QRect(0, 0, 196, 387))
        self.page_8.setObjectName("page_8")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.page_8)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.frame_20 = QtWidgets.QFrame(parent=self.page_8)
        self.frame_20.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.actionDES_GiaiMa = QtWidgets.QPushButton(parent=self.frame_20)
        self.actionDES_GiaiMa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionDES_GiaiMa.setObjectName("actionDES_GiaiMa")
        self.verticalLayout_25.addWidget(self.actionDES_GiaiMa)
        self.actionAES_GiaiMa = QtWidgets.QPushButton(parent=self.frame_20)
        self.actionAES_GiaiMa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionAES_GiaiMa.setObjectName("actionAES_GiaiMa")
        self.verticalLayout_25.addWidget(self.actionAES_GiaiMa)
        self.actionRSA_GiaiMa = QtWidgets.QPushButton(parent=self.frame_20)
        self.actionRSA_GiaiMa.setStyleSheet("background-color: rgb(242, 219, 116);\n"
"color:black;")
        self.actionRSA_GiaiMa.setObjectName("actionRSA_GiaiMa")
        self.verticalLayout_25.addWidget(self.actionRSA_GiaiMa)
        self.verticalLayout_24.addWidget(self.frame_20, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.toolBox.addItem(self.page_8, "")
        self.verticalLayout_8.addWidget(self.toolBox)

        self.retranslateUi(Dialog)
        self.toolBox.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnSaveFile.setText(_translate("Dialog", "Lưu file"))
        self.label_4.setText(_translate("Dialog", "Nội dung đã mã hoá:"))
        self.btnOpenFile.setText(_translate("Dialog", "Mở file"))
        self.label_2.setText(_translate("Dialog", "Nhập nội dung cần mã hoá:"))
        self.btnMaHoa.setText(_translate("Dialog", "Mã hoá"))
        self.label.setText(_translate("Dialog", "Mã hoá RSA"))
        self.btnClose.setText(_translate("Dialog", "Thoát"))
        self.actionHai_dong_MaHoa.setText(_translate("Dialog", "Chuyển vị hai dòng"))
        self.actionNhieu_dong_MaHoa.setText(_translate("Dialog", "Chuyển vị nhiều dòng"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Dialog", "Mã hóa chuyển vị"))
        self.actionCeasar_MaHoa.setText(_translate("Dialog", "Ceasar"))
        self.actionVignere_MaHoa.setText(_translate("Dialog", "Vignere"))
        self.actionBelasco_MaHoa.setText(_translate("Dialog", "Belasco"))
        self.actionTrithemius_MaHoa.setText(_translate("Dialog", "Trithemius"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Dialog", "Mã hóa thay thế"))
        self.actionXORCeasar_MaHoa.setText(_translate("Dialog", "Ceasar"))
        self.actionXORVignere_MaHoa.setText(_translate("Dialog", "Vignere"))
        self.actionXORBelasco_MaHoa.setText(_translate("Dialog", "Belasco"))
        self.actionXORTrithemius_MaHoa.setText(_translate("Dialog", "Trithemius"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("Dialog", "Mã hóa XOR"))
        self.actionDES_MaHoa.setText(_translate("Dialog", "SDES"))
        self.actionAES_MaHoa.setText(_translate("Dialog", "AES"))
        self.actionRSA_MaHoa.setText(_translate("Dialog", "RSA"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("Dialog", "Mã hóa hiện đại"))
        self.actionHai_dong_GiaiMa.setText(_translate("Dialog", "Chuyển vị 2 dòng"))
        self.actionNhieu_dong_GiaiMa.setText(_translate("Dialog", "Chuyển vị nhiều dòng"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), _translate("Dialog", "Giải mã chuyển vị"))
        self.actionCeasar_GiaiMa.setText(_translate("Dialog", "Ceasar"))
        self.actionVignere_GiaiMa.setText(_translate("Dialog", "Vignere"))
        self.actionBelasco_GiaiMa.setText(_translate("Dialog", "Belasco"))
        self.actionTrithemius_GiaiMa.setText(_translate("Dialog", "Trithemius"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), _translate("Dialog", "Giải mã thay thế"))
        self.actionXORCeasar_GiaiMa.setText(_translate("Dialog", "Ceasar"))
        self.actionXORVignere_GiaiMa.setText(_translate("Dialog", "Vignere"))
        self.actionXORBelasco_GiaiMa.setText(_translate("Dialog", "Belasco"))
        self.actionXORTrithemius_GiaiMa.setText(_translate("Dialog", "Trithemius"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_7), _translate("Dialog", "Giải mã XOR"))
        self.actionDES_GiaiMa.setText(_translate("Dialog", "SDES"))
        self.actionAES_GiaiMa.setText(_translate("Dialog", "AES"))
        self.actionRSA_GiaiMa.setText(_translate("Dialog", "RSA"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_8), _translate("Dialog", "Giải mã hiện đại"))
