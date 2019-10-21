# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/ui_02.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
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
        self.label04.setText(_translate("MainWindow", "ParkingLot 1"))
        self.label08.setText(_translate("MainWindow", "ParkingLot 1"))
        self.label01.setText(_translate("MainWindow", "ParkingLot 1"))
        self.label07.setText(_translate("MainWindow", "ParkingLot 1"))
        self.label03.setText(_translate("MainWindow", "ParkingLot 1"))
        self.label06.setText(_translate("MainWindow", "ParkingLot 1"))
        self.label05.setText(_translate("MainWindow", "ParkingLot 1"))
        self.label02.setText(_translate("MainWindow", "ParkingLot 1"))
        self.label.setText(_translate("MainWindow", "Exit"))

class myWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)



if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    w = myWin()
    w.show()
    sys.exit(app.exec_())
