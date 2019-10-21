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

if __name__ == "__main__":
    run()
