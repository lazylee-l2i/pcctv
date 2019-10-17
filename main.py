import cv2
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

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

class Mywin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn = QPushButton('여기를 눌러보시오', self)
        btn.resize(btn.sizeHint())
        btn.setToolTip('한번 만들어 보았습니다.<b>안녕하세요.<b/>')
        btn.move(20, 30)

        self.setGeometry(300,300,400,500)

        self.setWindowTitle('PCCTC!!S')

        self.show()



if __name__ == "__main__":
    #run()
    app = QApplication(sys.argv)
    w = Mywin()
    sys.exit(app.exec_())