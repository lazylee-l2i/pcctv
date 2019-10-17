import cv2
import numpy as np


class PCCTV:
    def __init__(self):
        self.imgDic = {}

    def imgshow(self, title='title', src='img'):
        cv2.imshow(title, src)

    def ROI(self, src='img', dst=None, sPoint=(0, 0), dPoint=(50, 50)):
        timg = np.zeros((200, 200, 3), np.uint8)
        timg[0:50, 0:50] = src[sPoint[0]:sPoint[1], dPoint[0]:dPoint[1]]
        if dst == None:
            return timg
        else:
            dst = timg

    def Threshold(self, src='img', dst=None, _min=200, _max=255):
        ret, timg = cv2.threshold(src, _min, _max, cv2.THRESH_BINARY_INV)
        if dst == None:
            return timg
        else:
            dst = timg

    def mkGray(self, src='img', dst=None):
        dst = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
        return dst

position_list = []
flag = 0
def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.line(param, (x,y), (x,y), (0,0,255), 5)
        position_list.append((x,y))
        if len(position_list) == 2:
            x1, y1 = position_list[0][0], position_list[0][1]
            x2, y2 = position_list[1][0], position_list[1][1]
            timg = np.zeros((x2 - x1, y2 - y1, 3), np.uint8)
            timg = param[]



def run():
    img = cv2.imread('./image/parkinglot/parkinglot_00.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    ret, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    canny = cv2.Canny(img, 200, 240)
    while True:
        cv2.imshow('origin', img)
        cv2.imshow('main', canny)
        k = cv2.waitKey(1) & 0xFF

        if k == 27:
            break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    run()