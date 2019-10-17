# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/ui__01.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 535)
        self.mFrame = QtWidgets.QFrame(Dialog)
        self.mFrame.setGeometry(QtCore.QRect(-10, -10, 1021, 531))
        self.mFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mFrame.setObjectName("mFrame")
        self.frame = QtWidgets.QFrame(self.mFrame)
        self.frame.setGeometry(QtCore.QRect(20, 20, 791, 501))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label04 = QtWidgets.QLabel(self.frame)
        self.label04.setGeometry(QtCore.QRect(610, 10, 171, 221))
        self.label04.setFrameShape(QtWidgets.QFrame.Box)
        self.label04.setAlignment(QtCore.Qt.AlignCenter)
        self.label04.setObjectName("label04")
        self.label08 = QtWidgets.QLabel(self.frame)
        self.label08.setGeometry(QtCore.QRect(610, 270, 171, 221))
        self.label08.setFrameShape(QtWidgets.QFrame.Box)
        self.label08.setAlignment(QtCore.Qt.AlignCenter)
        self.label08.setObjectName("label08")
        self.label01 = QtWidgets.QLabel(self.frame)
        self.label01.setGeometry(QtCore.QRect(10, 10, 171, 221))
        self.label01.setFrameShape(QtWidgets.QFrame.Box)
        self.label01.setAlignment(QtCore.Qt.AlignCenter)
        self.label01.setObjectName("label01")
        self.label07 = QtWidgets.QLabel(self.frame)
        self.label07.setGeometry(QtCore.QRect(410, 270, 171, 221))
        self.label07.setFrameShape(QtWidgets.QFrame.Box)
        self.label07.setAlignment(QtCore.Qt.AlignCenter)
        self.label07.setObjectName("label07")
        self.label03 = QtWidgets.QLabel(self.frame)
        self.label03.setGeometry(QtCore.QRect(410, 10, 171, 221))
        self.label03.setFrameShape(QtWidgets.QFrame.Box)
        self.label03.setAlignment(QtCore.Qt.AlignCenter)
        self.label03.setObjectName("label03")
        self.label06 = QtWidgets.QLabel(self.frame)
        self.label06.setGeometry(QtCore.QRect(210, 270, 171, 221))
        self.label06.setFrameShape(QtWidgets.QFrame.Box)
        self.label06.setAlignment(QtCore.Qt.AlignCenter)
        self.label06.setObjectName("label06")
        self.label05 = QtWidgets.QLabel(self.frame)
        self.label05.setGeometry(QtCore.QRect(10, 270, 171, 221))
        self.label05.setFrameShape(QtWidgets.QFrame.Box)
        self.label05.setAlignment(QtCore.Qt.AlignCenter)
        self.label05.setObjectName("label05")
        self.label02 = QtWidgets.QLabel(self.frame)
        self.label02.setGeometry(QtCore.QRect(210, 10, 171, 221))
        self.label02.setFrameShape(QtWidgets.QFrame.Box)
        self.label02.setAlignment(QtCore.Qt.AlignCenter)
        self.label02.setObjectName("label02")
        self.exLabel = QtWidgets.QLabel(self.mFrame)
        self.exLabel.setGeometry(QtCore.QRect(820, 30, 161, 481))
        font = QtGui.QFont()
        font.setPointSize(29)
        self.exLabel.setFont(font)
        self.exLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.exLabel.setTextFormat(QtCore.Qt.PlainText)
        self.exLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.exLabel.setObjectName("exLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label04.setText(_translate("Dialog", "ParkingLot 1"))
        self.label08.setText(_translate("Dialog", "ParkingLot 1"))
        self.label01.setText(_translate("Dialog", "ParkingLot 1"))
        self.label07.setText(_translate("Dialog", "ParkingLot 1"))
        self.label03.setText(_translate("Dialog", "ParkingLot 1"))
        self.label06.setText(_translate("Dialog", "ParkingLot 1"))
        self.label05.setText(_translate("Dialog", "ParkingLot 1"))
        self.label02.setText(_translate("Dialog", "ParkingLot 1"))
        self.exLabel.setText(_translate("Dialog", "Exit"))

class MyWindow(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
