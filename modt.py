# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/ui_02.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1021, 531)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mFrame = QtWidgets.QFrame(self.centralwidget)
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
        self.label = QtWidgets.QLabel(self.mFrame)
        self.label.setGeometry(QtCore.QRect(820, 30, 161, 481))
        font = QtGui.QFont()
        font.setPointSize(29)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label04.setText(_translate("MainWindow", "ParkingLot 4"))
        self.label08.setText(_translate("MainWindow", "ParkingLot 8"))
        self.label01.setText(_translate("MainWindow", "ParkingLot 1"))
        self.label07.setText(_translate("MainWindow", "ParkingLot 7"))
        self.label03.setText(_translate("MainWindow", "ParkingLot 3"))
        self.label06.setText(_translate("MainWindow", "ParkingLot 6"))
        self.label05.setText(_translate("MainWindow", "ParkingLot 5"))
        self.label02.setText(_translate("MainWindow", "ParkingLot 2"))
        self.label.setText(_translate("MainWindow", "Exit"))

from PLotModule.receiveData import Thread

class myWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.t = Thread()
        self.t.start()

        self.t.chagned_text.connect(self.change_label)

    @pyqtSlot(str)
    def change_label(self, _text):
        if _text[0] == '1':
            self.label01.setText('True')
        else:
            self.label01.setText('ParkingLot 1')
        if _text[1] == '1':
            self.label02.setText('True')
        else:
            self.label02.setText('ParkingLot 2')
        if _text[2] == '1':
            self.label03.setText('True')
        else:
            self.label03.setText('ParkingLot 3')
        if _text[3] == '1':
            self.label04.setText('True')
        else:
            self.label04.setText('ParkingLot 4')
        if _text[4] == '1':
            self.label05.setText('True')
        else:
            self.label05.setText('ParkingLot 5')
        if _text[5] == '1':
            self.label06.setText('True')
        else:
            self.label06.setText('ParkingLot 6')
        if _text[6] == '1':
            self.label07.setText('True')
        else:
            self.label07.setText('ParkingLot 7')
        if _text[7] == '1':
            self.label08.setText('True')
        else:
            self.label08.setText('ParkingLot 8')
if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    w = myWin()
    w.show()
    sys.exit(app.exec_())
