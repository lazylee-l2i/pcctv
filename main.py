import cv2
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

RED = (0,0,255)
position_list = []

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.line(param, (x,y), (x,y), RED, 5)
        position_list.append((x,y))
        print(position_list)



def run():
    imag = cv2.imread("./image/polite_cat_02.jpg")
    cv2.namedWindow('cat')
    cv2.setMouseCallback('cat', onMouse, param=imag)


    while True:
        cv2.imshow('cat', imag)
        k = cv2.waitKey(1) & 0xFF

        if k == 27:
            break
    cv2.destroyAllWindows()

import socket
import threading



class Mywin(QWidget):
    def __init__(self):
        super().__init__()
        self.sock = socket.socket(socket.AF_INET,
                             socket.SOCK_STREAM)
        self.sock.bind(('localhost', 0))
        self.sock.connect(('localhost', 5425))
        self.initUI()

    def initUI(self):
        btn = QPushButton('여기를 눌러보시오', self)
        btn.resize(btn.sizeHint())
        btn.setToolTip('한번 만들어 보았습니다.<b>안녕하세요.<b/>')
        btn.move(20, 30)
        self.label = QLabel('테스트', self)
        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle('PCCTC!!S')
        self.run()
        self.show()

    def run(self):
        try:
            message = self.sock.recv(1024)
            message = str(message, encoding='utf-8')
            self.label.setText('수신 메세지 : ' + message)
        finally:
            if message == 'q':
                self.sock.close()
            else:
                pass



if __name__ == "__main__":
    #run()
    app = QApplication(sys.argv)
    w = Mywin()
    sys.exit(app.exec_())