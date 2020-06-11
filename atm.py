# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'atmgui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 651)
        MainWindow.setStyleSheet("background-color:#a6a6a6")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 540, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:#bfbfbf")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 540, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:#bfbfbf")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 540, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color:#bfbfbf")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 480, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color:#bfbfbf")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(290, 480, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color:#bfbfbf")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(370, 480, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color:#bfbfbf")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(210, 420, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color:#bfbfbf")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(290, 420, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color:#bfbfbf")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(370, 420, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color:#bfbfbf")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(210, 360, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color:#bfbfbf")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(290, 360, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color:#bfbfbf")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(370, 360, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color:#bfbfbf")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(450, 480, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("background-color:green;\n"
"border-radius: 15px;")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(450, 420, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color:yellow;\n"
"border-radius: 15px;")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(450, 360, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("background-color:red;\n"
"border-radius: 15px;")
        self.pushButton_15.setObjectName("pushButton_15")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(190, 340, 381, 261))
        self.frame.setStyleSheet("background-color:#a6a6a6;\n"
"border-radius:10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(70, 20, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Chaparral Pro Light")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("text-align:right;\n"
"background-color:#bfbfbf;\n"
"border-radius:10px;\n"
"border: 2px solid white;")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(70, 90, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Chaparral Pro Light")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("text-align:right;\n"
"background-color:#bfbfbf;\n"
"border-radius:10px;\n"
"border: 2px solid white;")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(70, 160, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Chaparral Pro Light")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("text-align:right;\n"
"background-color:#bfbfbf;\n"
"border-radius:10px;\n"
"border: 2px solid white;")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(70, 230, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Chaparral Pro Light")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("text-align:right;\n"
"background-color:#bfbfbf;\n"
"border-radius:10px;\n"
"border: 2px solid white;")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(660, 20, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Chaparral Pro Light")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("text-align:left;\n"
"border: 2px solid white;\n"
"border-radius:10px;\n"
"background-color:#bfbfbf;")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(660, 90, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Chaparral Pro Light")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("text-align:left;\n"
"border: 2px solid white;\n"
"border-radius:10px;\n"
"background-color:#bfbfbf;")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(660, 160, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Chaparral Pro Light")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setStyleSheet("text-align:left;\n"
"border: 2px solid white;\n"
"border-radius:10px;\n"
"background-color:#bfbfbf;")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(660, 230, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Chaparral Pro Light")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setStyleSheet("text-align:left;\n"
"border: 2px solid white;\n"
"border-radius:10px;\n"
"background-color:#bfbfbf;")
        self.pushButton_23.setObjectName("pushButton_23")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 310, 801, 321))
        self.frame_2.setStyleSheet("background-color:#d9d9d9")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(140, 10, 511, 281))
        self.frame_3.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"background-image: url(bgim.png)")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.textEdit = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit.setGeometry(QtCore.QRect(0, 10, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 80, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit_3.setGeometry(QtCore.QRect(0, 150, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit_4.setGeometry(QtCore.QRect(0, 220, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit_5.setGeometry(QtCore.QRect(370, 10, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.textEdit_5.setFont(font)
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_9 = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit_9.setGeometry(QtCore.QRect(160, 90, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.textEdit_9.setFont(font)
        self.textEdit_9.setStyleSheet("")
        self.textEdit_9.setObjectName("textEdit_9")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setGeometry(QtCore.QRect(200, 180, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setText("")
        self.lineEdit.setFrame(True)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("border: 0.5px solid black;border-radius:5px;")
        self.lineEdit.hide()
        self.textEdit_6 = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit_6.setGeometry(QtCore.QRect(370, 80, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.textEdit_6.setFont(font)
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit_7.setGeometry(QtCore.QRect(370, 150, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.textEdit_7.setFont(font)
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_8 = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit_8.setGeometry(QtCore.QRect(370, 220, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.textEdit_8.setFont(font)
        self.textEdit_8.setObjectName("textEdit_8")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(100, 210, 301, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color:red")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(150, 210, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:red")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(150, 160, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:red")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 179, 221, 31))
        self.lineEdit_2.setStyleSheet("font-family:\'Consolas\';\n"
"font-size:14pt;\n"
"font-weight:400;\n"
"font-style:normal;")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("border: 0.5px solid black;border-radius:5px;")
        self.lineEdit_2.hide()
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(120, 160, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:red")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.textEdit_9.raise_()
        self.textEdit_3.raise_()
        self.textEdit_2.raise_()
        self.textEdit.raise_()
        self.textEdit_4.raise_()
        self.textEdit_5.raise_()
        self.textEdit_6.raise_()
        self.textEdit_7.raise_()
        self.textEdit_8.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.frame.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.pushButton_11.raise_()
        self.pushButton_12.raise_()
        self.pushButton_13.raise_()
        self.pushButton_14.raise_()
        self.pushButton_15.raise_()
        self.pushButton_16.raise_()
        self.pushButton_17.raise_()
        self.pushButton_18.raise_()
        self.pushButton_19.raise_()
        self.pushButton_20.raise_()
        self.pushButton_21.raise_()
        self.pushButton_22.raise_()
        self.pushButton_23.raise_()
        
        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        ##########################
        self.textEdit_9.clear()
        self.textEdit_9.append("Saisissez votre mot de passe :")
        self.lineEdit.show()

########################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ATM"))
        self.pushButton.setText(_translate("MainWindow", "0"))
        self.pushButton_2.setText(_translate("MainWindow", "."))
        self.pushButton_3.setText(_translate("MainWindow", "00"))
        self.pushButton_4.setText(_translate("MainWindow", "1"))
        self.pushButton_5.setText(_translate("MainWindow", "2"))
        self.pushButton_6.setText(_translate("MainWindow", "3"))
        self.pushButton_7.setText(_translate("MainWindow", "4"))
        self.pushButton_8.setText(_translate("MainWindow", "5"))
        self.pushButton_9.setText(_translate("MainWindow", "6"))
        self.pushButton_10.setText(_translate("MainWindow", "7"))
        self.pushButton_11.setText(_translate("MainWindow", "8"))
        self.pushButton_12.setText(_translate("MainWindow", "9"))
        self.pushButton_13.setText(_translate("MainWindow", "ENTER"))
        self.pushButton_14.setText(_translate("MainWindow", "CLEAR"))
        self.pushButton_15.setText(_translate("MainWindow", "CANCEL"))
        self.pushButton_16.setText(_translate("MainWindow", ">"))
        self.pushButton_17.setText(_translate("MainWindow", ">"))
        self.pushButton_18.setText(_translate("MainWindow", ">"))
        self.pushButton_19.setText(_translate("MainWindow", ">"))
        self.pushButton_20.setText(_translate("MainWindow", "<"))
        self.pushButton_21.setText(_translate("MainWindow", "<"))
        self.pushButton_22.setText(_translate("MainWindow", "<"))
        self.pushButton_23.setText(_translate("MainWindow", "<"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        
        self.textEdit_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        
        self.textEdit_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        
        self.textEdit_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Votre mot de passe doit comporter 4 chiffres!!"))
        self.label_2.setText(_translate("MainWindow", "Ce mots de passe est errone"))
        self.label_3.setText(_translate("MainWindow", "Ceci est le mot de passe actuel!"))
        self.label_4.setText(_translate("MainWindow", "Le numero doit comporter 24 chiffres!!"))

    def __init__(self):
        self.n=3
        self.it1=0
        self.page="main"
        self.solde=300.00
        self.trans=0
        self.mdp="1234"
        self.temp=""
        self.temp2=""

    def keyboard(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        tempword=''
        if self.page=="main":
            for i in word:
                tempword=tempword+str(i)
                self.lineEdit.setText(tempword)
        elif self.page=="autremontant":
            for j in word:
                tempword=tempword+str(j)
                self.lineEdit_2.setText(tempword)
        elif self.page=="transfert":
            for j in word:
                tempword=tempword+str(j)
                self.lineEdit_2.setText(tempword)
        elif self.page=="transfertrib":
            for j in word:
                tempword=tempword+str(j)
                self.lineEdit_2.setText(tempword)
        elif self.page=="changermdp":
            for j in word:
                tempword=tempword+str(j)
                self.lineEdit.setText(tempword)
        elif self.page=="confirmermdp":
            for j in word:
                tempword=tempword+str(j)
                self.lineEdit.setText(tempword)
        elif self.page=="sim1":
            for j in word:
                tempword=tempword+str(j)
                self.lineEdit_2.setText(tempword)
        elif self.page=="sim2":
            for j in word:
                tempword=tempword+str(j)
                self.lineEdit_2.setText(tempword)
            
    def check_mdp(self):
        global mdps
        mdps=self.lineEdit.text()	#la premiere saisie du mot de passe
        if mdps != self.mdp:
            if len(mdps) != 4:
                self.label.show()
                self.label_2.hide()
                self.label_3.hide()
                self.label_4.hide()
                mdps=self.lineEdit.text()
                self.n-=1
            elif len(mdps) == 4:
                self.label.hide()
                self.label_2.show()
                self.label_3.hide()
                self.label_4.hide()
                mdps=self.lineEdit.text()
                self.n-=1
        if self.n==0 and mdps != self.mdp:
            self.textEdit_9.clear()
            self.textEdit_9.append("La carte a ete saisie, contactez votre banque!")
            self.lineEdit.clear()
            self.lineEdit.hide()
            self.label.hide()
            self.label_2.hide()
            self.label_3.hide()
            self.label_4.hide()
        if mdps == self.mdp:
            global actif
            actif=True			#la session est active
            self.textEdit_9.hide()
            self.lineEdit.hide()
            self.label.hide()
            self.label_2.hide()
            self.label_3.hide()
            self.label_4.hide()
            self.menu()

    def menu(self):
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.textEdit_3.clear()
        self.textEdit_4.clear()
        self.textEdit_5.clear()
        self.textEdit_6.clear()
        self.textEdit_7.clear()
        self.textEdit_8.clear()
        self.textEdit_9.clear()
        self.textEdit.append("Retirer de l'argent")
        self.textEdit_2.append("Consulter votre compte")
        self.textEdit_3.append("Transfert d'argent")
        self.textEdit_4.append("Changer de mot de de passe")
        self.textEdit_5.append("Simulation de credit")
        #global page
        self.page="main"
        
    def retirer_menu(self):
        _translate = QtCore.QCoreApplication.translate
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.textEdit_3.clear()
        self.textEdit_4.clear()
        self.textEdit.append("200 Dhs")
        self.textEdit_2.append("400 Dhs")
        self.textEdit_3.append("500 Dhs")
        self.textEdit_4.append("600 Dhs")
        self.textEdit_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_5.append("900 Dhs")
        self.textEdit_6.append("1200 Dhs")
        self.textEdit_7.append("Autre montant")
        self.textEdit_8.append("Retour au menu")
        #global page
        self.page="montants"
    
    def consulter(self):
        _translate = QtCore.QCoreApplication.translate
        self.textEdit_9.clear()
        self.textEdit_9.show()
        self.textEdit_9.append("Votre solde est de "+str(self.solde)+" Dhs")
        self.textEdit.hide()
        self.textEdit_2.hide()
        self.textEdit_3.hide()
        self.textEdit_4.hide()
        self.textEdit_5.hide()
        self.textEdit_6.hide()
        self.textEdit_7.hide()
        self.textEdit_8.show()
        self.textEdit_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_8.append("Retour au menu")
        self.page="consulter"
    
    def transfertrib(self):
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.textEdit_9.clear()
        self.textEdit_9.show()
        self.textEdit_9.append("Le numero de compte du destinataire :")
        self.textEdit.hide()
        self.textEdit_2.hide()
        self.textEdit_3.hide()
        self.textEdit_4.show()
        self.textEdit_4.clear()
        self.textEdit_4.append("Valider")
        self.textEdit_5.hide()
        self.textEdit_6.hide()
        self.textEdit_7.hide()
        self.textEdit_8.show()
        self.textEdit_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_8.append("Retour au menu")
        self.lineEdit_2.show()
        self.page="transfertrib"
    
    def transfertmontant(self):
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.textEdit_9.clear()
        self.textEdit_9.show()
        self.textEdit_9.append("Le montant a tranferer :")
        self.textEdit.hide()
        self.textEdit_2.hide()
        self.textEdit_3.hide()
        self.textEdit_4.hide()
        self.textEdit_5.hide()
        self.textEdit_6.hide()
        self.textEdit_7.hide()
        self.textEdit_8.show()
        self.textEdit_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_8.append("Retour au menu")
        self.lineEdit_2.show()
        self.page="transfert"
    
    def check_transfert(self):
        global numcpte
        numcpte=self.lineEdit_2.text()
        if len(numcpte) != 24:
            self.label_4.show()
            numcpte=self.lineEdit_2.text()
        elif self.trans > self.solde:
            self.label_4.hide()
            self.lineEdit_2.hide()
            self.textEdit_4.hide()
            self.textEdit_9.clear()
            self.textEdit_9.append("Vous ne pouvez pas transferer plus de "+str(self.solde)+" Dhs")
        else:
            self.solde=self.solde-self.trans
            self.label_4.hide()
            self.lineEdit_2.hide()
            self.textEdit_4.hide()
            self.textEdit_9.clear()
            self.textEdit_9.append("Transfert reussi.")
    
    def changermdp(self):
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.textEdit_9.clear()
        self.textEdit_9.show()
        self.textEdit_9.append("Entrez le nouveau mot de passe :")
        self.textEdit.hide()
        self.textEdit_2.hide()
        self.textEdit_3.hide()
        self.textEdit_4.hide()
        self.textEdit_5.hide()
        self.textEdit_6.hide()
        self.textEdit_7.hide()
        self.textEdit_8.show()
        self.textEdit_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_8.append("Retour au menu")
        self.lineEdit.show()
        self.page="changermdp"
    
    
    def confirmermdp(self):
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.textEdit_9.clear()
        self.textEdit_9.show()
        self.textEdit_9.append("Confirmez le nouveau mot de passe :")
        self.textEdit.hide()
        self.textEdit_2.hide()
        self.textEdit_3.hide()
        self.textEdit_4.show()
        self.textEdit_4.clear()
        self.textEdit_4.append("Valider")
        self.textEdit_5.hide()
        self.textEdit_6.hide()
        self.textEdit_7.hide()
        self.textEdit_8.show()
        self.textEdit_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_8.append("Retour au menu")
        self.lineEdit.show()
        self.label.hide()
        self.label_3.hide()
        self.page="confirmermdp"
    
    def sim_montant(self):
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.textEdit_9.clear()
        self.textEdit_9.show()
        self.textEdit_9.append("Le montant demande:")
        self.textEdit.hide()
        self.textEdit_2.hide()
        self.textEdit_3.hide()
        self.textEdit_4.hide()
        self.textEdit_5.hide()
        self.textEdit_6.hide()
        self.textEdit_7.hide()
        self.textEdit_8.show()
        self.textEdit_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_8.append("Retour au menu")
        self.lineEdit_2.show()
        self.label.hide()
        self.label_3.hide()
        self.page="sim1"
        
    def sim_duree(self):
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.textEdit_9.clear()
        self.textEdit_9.show()
        self.textEdit_9.append("La duree du credit (en mois) :")
        self.textEdit.hide()
        self.textEdit_2.hide()
        self.textEdit_3.hide()
        self.textEdit_4.show()
        self.textEdit_4.clear()
        self.textEdit_4.append("Valider")
        self.textEdit_5.hide()
        self.textEdit_6.hide()
        self.textEdit_7.hide()
        self.textEdit_8.show()
        self.textEdit_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_8.append("Retour au menu")
        self.lineEdit_2.show()
        self.label.hide()
        self.label_3.hide()
        self.page="sim2"
    
    
    def action1(self):
        self.it1+=1
        if self.page=="main":
            self.retirer_menu()
            self.it1+=1
        if self.page=="montants" and self.it1%2==1 :
            ret=200
            self.it1+=1
            if ret > self.solde:
                self.textEdit_9.clear()
                self.textEdit_9.show()
                self.textEdit_9.append("Vous ne pouvez pas retirer plus de "+str(self.solde)+" Dhs")
                self.textEdit.hide()
                self.textEdit_2.hide()
                self.textEdit_3.hide()
                self.textEdit_4.hide()
                self.textEdit_5.hide()
                self.textEdit_6.hide()
                self.textEdit_7.hide()
                self.textEdit_8.show()
            else:
                
                self.solde=self.solde-ret
                self.textEdit_9.clear()
                self.textEdit_9.show()
                self.textEdit.hide()
                self.textEdit_2.hide()
                self.textEdit_3.hide()
                self.textEdit_4.hide()
                self.textEdit_5.hide()
                self.textEdit_6.hide()
                self.textEdit_7.hide()
                self.textEdit_8.hide()
                self.ticket()
    
    def action2(self):
        self.it1+=1
        if self.page=="main":
            self.consulter()
            self.it1+=1
        if self.page=="montants" and self.it1%2==1 :
            ret=400
            self.it1+=1
            if ret > self.solde:
                self.textEdit_9.clear()
                self.textEdit_9.show()
                self.textEdit_9.append("Vous ne pouvez pas retirer plus de "+str(self.solde)+" Dhs")
                self.textEdit.hide()
                self.textEdit_2.hide()
                self.textEdit_3.hide()
                self.textEdit_4.hide()
                self.textEdit_5.hide()
                self.textEdit_6.hide()
                self.textEdit_7.hide()
                self.textEdit_8.show()
            else:
                
                self.solde=self.solde-ret
                self.textEdit_9.clear()
                self.textEdit_9.show()
                self.textEdit.hide()
                self.textEdit_2.hide()
                self.textEdit_3.hide()
                self.textEdit_4.hide()
                self.textEdit_5.hide()
                self.textEdit_6.hide()
                self.textEdit_7.hide()
                self.textEdit_8.hide()
                self.ticket()
    def action3(self):
        self.it1+=1
        if self.page=="main":
            self.transfertmontant()
            self.it1+=1
        if self.page=="montants" and self.it1%2==1 :
            ret=500
            self.it1+=1
            if ret > self.solde:
                self.textEdit_9.clear()
                self.textEdit_9.show()
                self.textEdit_9.append("Vous ne pouvez pas retirer plus de "+str(self.solde)+" Dhs")
                self.textEdit.hide()
                self.textEdit_2.hide()
                self.textEdit_3.hide()
                self.textEdit_4.hide()
                self.textEdit_5.hide()
                self.textEdit_6.hide()
                self.textEdit_7.hide()
                self.textEdit_8.show()
            else:
                
                self.solde=self.solde-ret
                self.textEdit_9.clear()
                self.textEdit_9.show()
                self.textEdit.hide()
                self.textEdit_2.hide()
                self.textEdit_3.hide()
                self.textEdit_4.hide()
                self.textEdit_5.hide()
                self.textEdit_6.hide()
                self.textEdit_7.hide()
                self.textEdit_8.hide()
                self.ticket()
    
    def action4(self):
        self.it1+=1
        if self.page=="main":
            self.changermdp()
            self.it1+=1
        if self.page=="montants" and self.it1%2==1 :
            ret=600
            self.it1+=1
            if ret > self.solde:
                self.textEdit_9.clear()
                self.textEdit_9.show()
                self.textEdit_9.append("Vous ne pouvez pas retirer plus de "+str(self.solde)+" Dhs")
                self.textEdit.hide()
                self.textEdit_2.hide()
                self.textEdit_3.hide()
                self.textEdit_4.hide()
                self.textEdit_5.hide()
                self.textEdit_6.hide()
                self.textEdit_7.hide()
                self.textEdit_8.show()
            else:
                
                self.solde=self.solde-ret
                self.textEdit_9.clear()
                self.textEdit_9.show()
                self.textEdit.hide()
                self.textEdit_2.hide()
                self.textEdit_3.hide()
                self.textEdit_4.hide()
                self.textEdit_5.hide()
                self.textEdit_6.hide()
                self.textEdit_7.hide()
                self.textEdit_8.hide()
                self.ticket()
        
        if self.page=="transfertrib":
            self.check_transfert()
        
        if self.page=="sim2":
            self.temp2=int(self.lineEdit_2.text())
            t=0.045			#le taux d interet (4.5%)
            m=(self.temp*t/12)/(1-(1+t/12)**(-self.temp2))		#la mensualité
            print("") #affiche le mensualité arrondie
            self.textEdit_9.clear()
            self.textEdit_9.show()
            self.textEdit_9.append("Vous aurez a payer "+str(round(m,2))+" Dhs par mois.")
            self.textEdit.hide()
            self.textEdit_2.hide()
            self.textEdit_3.hide()
            self.textEdit_4.hide()
            self.textEdit_5.hide()
            self.textEdit_6.hide()
            self.textEdit_7.hide()
            self.textEdit_8.show()
            self.lineEdit_2.hide()
        if self.page=="ticket":
            self.textEdit_9.clear()
            self.textEdit_9.show()
            self.textEdit_9.append("Recuperez votre argent et votre ticket.\tAu revoir.")
            self.textEdit.hide()
            self.textEdit_2.hide()
            self.textEdit_3.hide()
            self.textEdit_4.hide()
            self.textEdit_5.hide()
            self.textEdit_6.hide()
            self.textEdit_7.hide()
            self.textEdit_8.hide()
            
        if self.page=="confirmermdp":
            self.temp2=self.lineEdit.text()
            if self.temp == self.temp2 :
                self.mdp=self.temp2
                _translate = QtCore.QCoreApplication.translate
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.textEdit_9.clear()
                self.textEdit_9.show()
                self.textEdit_9.append("Votre mot de passe a ete modifie avec succes.")
                self.textEdit.hide()
                self.textEdit_2.hide()
                self.textEdit_3.hide()
                self.textEdit_4.hide()
                self.textEdit_5.hide()
                self.textEdit_6.hide()
                self.textEdit_7.hide()
                self.textEdit_8.show()
                self.textEdit_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textEdit_8.append("Retour au menu")
                self.lineEdit.hide()
            if self.temp != self.temp2:
                _translate = QtCore.QCoreApplication.translate
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.textEdit_9.clear()
                self.textEdit_9.show()
                self.textEdit_9.append("Le mots de passe n'a pas ete modifie.")
                self.textEdit.hide()
                self.textEdit_2.hide()
                self.textEdit_3.hide()
                self.textEdit_4.hide()
                self.textEdit_5.hide()
                self.textEdit_6.hide()
                self.textEdit_7.hide()
                self.textEdit_8.show()
                self.textEdit_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                self.textEdit_8.append("Retour au menu")
                self.lineEdit.hide()
        
    def action5(self):
        self.it1+=1
        if self.page=="main":
            self.sim_montant()
            self.it1+=1
        if self.page=="montants" and self.it1%2==1 :
            ret=900
            self.it1+=1
            if ret > self.solde:
                self.textEdit_9.clear()
                self.textEdit_9.show()
                self.textEdit_9.append("Vous ne pouvez pas retirer plus de "+str(self.solde)+" Dhs")
                self.textEdit.hide()
                self.textEdit_2.hide()
                self.textEdit_3.hide()
                self.textEdit_4.hide()
                self.textEdit_5.hide()
                self.textEdit_6.hide()
                self.textEdit_7.hide()
                self.textEdit_8.show()
            else:
                
                self.solde=self.solde-ret
                self.textEdit_9.clear()
                self.textEdit_9.show()
                self.textEdit.hide()
                self.textEdit_2.hide()
                self.textEdit_3.hide()
                self.textEdit_4.hide()
                self.textEdit_5.hide()
                self.textEdit_6.hide()
                self.textEdit_7.hide()
                self.textEdit_8.hide()
                self.ticket()
                
                
                
    def action6(self):
        self.it1+=1
        if self.page=="montants":
            ret=1200
            self.it1+=1
            if ret > self.solde:
                self.textEdit_9.clear()
                self.textEdit_9.show()
                self.textEdit_9.append("Vous ne pouvez pas retirer plus de "+str(self.solde)+" Dhs")
                self.textEdit.hide()
                self.textEdit_2.hide()
                self.textEdit_3.hide()
                self.textEdit_4.hide()
                self.textEdit_5.hide()
                self.textEdit_6.hide()
                self.textEdit_7.hide()
                self.textEdit_8.show()
            else:
                
                self.solde=self.solde-ret
                self.textEdit_9.clear()
                self.textEdit_9.show()
                self.textEdit.hide()
                self.textEdit_2.hide()
                self.textEdit_3.hide()
                self.textEdit_4.hide()
                self.textEdit_5.hide()
                self.textEdit_6.hide()
                self.textEdit_7.hide()
                self.textEdit_8.hide()
                self.ticket()
    
    def action7(self):
        
        if self.page=="montants":
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.textEdit_9.clear()
            self.textEdit_9.show()
            self.textEdit_9.append("Saisissez le montant a retirer :")
            self.textEdit.hide()
            self.textEdit_2.hide()
            self.textEdit_3.hide()
            self.textEdit_4.hide()
            self.textEdit_5.hide()
            self.textEdit_6.hide()
            self.textEdit_7.hide()
            self.textEdit_8.hide()
            self.lineEdit_2.show()
            self.page="autremontant"
    
    def action8(self):
        if self.page=="ticket":
            self.textEdit_9.clear()
            self.textEdit_9.show()
            self.textEdit_9.append("Recuperez votre argent et votre carte.\tAu revoir.")
            self.textEdit.hide()
            self.textEdit_2.hide()
            self.textEdit_3.hide()
            self.textEdit_4.hide()
            self.textEdit_5.hide()
            self.textEdit_6.hide()
            self.textEdit_7.hide()
            self.textEdit_8.hide()
        if self.page=="montants" or self.page=="autremontant" or self.page=="consulter" or self.page=="transfert" or self.page=="transfertrib" or self.page=="changermdp" or self.page=="confirmermdp" or self.page=="sim1" or self.page=="sim2":
            self.textEdit.show()
            self.textEdit_2.show()
            self.textEdit_3.show()
            self.textEdit_4.show()
            self.textEdit_5.show()
            self.textEdit_6.show()
            self.textEdit_7.show()
            self.textEdit_8.show()
            self.lineEdit.hide()
            self.lineEdit_2.hide()
            self.it1=0
            self.menu()
            
            
    def actionenter(self):
        if self.page=="main":
            self.check_mdp()
        if self.page=="autremontant":
            ret=float(self.lineEdit_2.text())
            if ret > self.solde:
                self.textEdit_9.clear()
                self.textEdit_9.show()
                self.textEdit_9.append("Vous ne pouvez pas retirer plus de "+str(self.solde)+" Dhs")
                self.textEdit.hide()
                self.textEdit_2.hide()
                self.textEdit_3.hide()
                self.textEdit_4.hide()
                self.textEdit_5.hide()
                self.textEdit_6.hide()
                self.textEdit_7.hide()
                self.textEdit_8.show()
                self.lineEdit_2.hide()
            elif self.solde>=2500 and ret>2500:
                self.textEdit_9.clear()
                self.textEdit_9.show()
                self.textEdit_9.append("Vous ne pouvez pas retirer plus de 2500 Dhs")
                self.textEdit.hide()
                self.textEdit_2.hide()
                self.textEdit_3.hide()
                self.textEdit_4.hide()
                self.textEdit_5.hide()
                self.textEdit_6.hide()
                self.textEdit_7.hide()
                self.textEdit_8.show()
                self.lineEdit_2.hide()
            else:
                self.solde=self.solde-ret
                self.textEdit_9.clear()
                self.textEdit_9.show()
                self.textEdit.hide()
                self.textEdit_2.hide()
                self.textEdit_3.hide()
                self.textEdit_4.hide()
                self.textEdit_5.hide()
                self.textEdit_6.hide()
                self.textEdit_7.hide()
                self.textEdit_8.hide()
                self.ticket()
        if self.page=="transfert":
            self.trans=float(self.lineEdit_2.text())
            self.transfertrib()
        if self.page=="changermdp":
            self.label.hide()
            self.label_3.hide()
            self.temp=self.lineEdit.text()
            if self.temp == self.mdp or len(self.temp) != 4:
                if len(self.temp) != 4:
                    self.label.show()
                elif self.temp == self.mdp :
                    self.label_3.show()
            else:
                self.confirmermdp()
        if self.page=="sim1":
            self.temp=int(self.lineEdit_2.text())
            self.sim_duree()

    
    def actioncancel(self):
        self.textEdit_9.clear()
        self.textEdit_9.show()
        self.textEdit_9.append("Recuperez votre carte.\tAu revoir")
        self.textEdit.hide()
        self.textEdit_2.hide()
        self.textEdit_3.hide()
        self.textEdit_4.hide()
        self.textEdit_5.hide()
        self.textEdit_6.hide()
        self.textEdit_7.hide()
        self.textEdit_8.hide()
        self.lineEdit_2.hide()
        self.lineEdit.hide()
        self.lineEdit_2.hide()
        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.page="fin"
    
    def ticket(self):
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit_2.hide()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.textEdit_9.clear()
        self.textEdit_9.append("Voulez vous un ticket?")
        self.textEdit_4.show()
        self.textEdit_4.clear()
        self.textEdit_4.append("OUI")
        self.textEdit_8.show()
        self.textEdit_8.clear()
        self.textEdit_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_8.append("NON")
        #global page
        self.page="ticket"
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #################################################################################
    ui.pushButton_16.clicked.connect(ui.action1)
    ui.pushButton_17.clicked.connect(ui.action2)
    ui.pushButton_18.clicked.connect(ui.action3)
    ui.pushButton_19.clicked.connect(ui.action4)
    ui.pushButton_20.clicked.connect(ui.action5)
    ui.pushButton_21.clicked.connect(ui.action6)
    ui.pushButton_22.clicked.connect(ui.action7)
    ui.pushButton_23.clicked.connect(ui.action8)
    ui.pushButton_13.clicked.connect(ui.actionenter)
    ui.pushButton_15.clicked.connect(ui.actioncancel)
    ###################################################################################
    ###################################################################################
    word=[]

    ui.pushButton.clicked.connect(lambda: word.append('0'))
    ui.pushButton.clicked.connect(ui.keyboard)
    ui.pushButton_2.clicked.connect(lambda: word.append('.'))
    ui.pushButton_2.clicked.connect(ui.keyboard)
    ui.pushButton_3.clicked.connect(lambda: word.append('00'))
    ui.pushButton_3.clicked.connect(ui.keyboard)
    ui.pushButton_4.clicked.connect(lambda: word.append('1'))
    ui.pushButton_4.clicked.connect(ui.keyboard)
    ui.pushButton_5.clicked.connect(lambda: word.append('2'))
    ui.pushButton_5.clicked.connect(ui.keyboard)
    ui.pushButton_6.clicked.connect(lambda: word.append('3'))
    ui.pushButton_6.clicked.connect(ui.keyboard)
    ui.pushButton_7.clicked.connect(lambda: word.append('4'))
    ui.pushButton_7.clicked.connect(ui.keyboard)
    ui.pushButton_8.clicked.connect(lambda: word.append('5'))
    ui.pushButton_8.clicked.connect(ui.keyboard)
    ui.pushButton_9.clicked.connect(lambda: word.append('6'))
    ui.pushButton_9.clicked.connect(ui.keyboard)
    ui.pushButton_10.clicked.connect(lambda: word.append('7'))
    ui.pushButton_10.clicked.connect(ui.keyboard)
    ui.pushButton_11.clicked.connect(lambda: word.append('8'))
    ui.pushButton_11.clicked.connect(ui.keyboard)
    ui.pushButton_12.clicked.connect(lambda: word.append('9'))
    ui.pushButton_12.clicked.connect(ui.keyboard)
    ui.pushButton_14.clicked.connect(ui.lineEdit.clear)
    ui.pushButton_14.clicked.connect(lambda: word.clear())
    ui.pushButton_18.clicked.connect(lambda: word.clear())
    ui.pushButton_22.clicked.connect(lambda: word.clear())
    ui.pushButton_13.clicked.connect(lambda: word.clear())
    ui.pushButton_19.clicked.connect(lambda: word.clear())
    ui.pushButton_14.clicked.connect(ui.lineEdit_2.clear)

    

    
    
    MainWindow.show()
    sys.exit(app.exec_())
