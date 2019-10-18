import cv2
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtCore import QThread, pyqtSignal,QWaitCondition, QMutex

import socket
class Thread(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.message = ' '
        self.sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM)
        self.sock.bind(('localhost', 0))
        self.sock.connect(('localhost', 5425))

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            #To Do
            try:
                message = self.sock.recv(1024)
                message = str(message, encoding='utf-8')
                self.message = message
            finally:
                if self.message == 'q':
                    self.sock.close()

class Mywin(QWidget):
    def __init__(self):
        super().__init__()

        self.th = Thread()
        self.btn = QPushButton('여기를 눌러보시오', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.setToolTip('한번 만들어 보았습니다.<b>안녕하세요.<b/>')
        self.btn.move(20, 30)
        self.label = QLabel('테스트', self)
        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle('PCCTC!!S')
        self.initUI()
        self.th.start()

    def initUI(self):
        self.label.setText(self.th.message)


if __name__ == "__main__":
    #run()
    app = QApplication(sys.argv)
    w = Mywin()
    w.show()
    sys.exit(app.exec_())