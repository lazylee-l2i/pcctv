import sys
import os
from PyQt5 import uic

def compile_ui(UI_PATH='Insert UI path'):
    if not os.path.exists(UI_PATH):
        print("File is not exists!")
        return
    uiPyFile = os.path.splitext(UI_PATH)[0] + '.py'
    print(uiPyFile)
    fp = open(uiPyFile, 'w')

    uic.compileUi(UI_PATH, fp, from_imports=True)
    fp.close()

if __name__ == '__main__':
    UI_PATH = './UI/ui_02.ui'
    compile_ui(UI_PATH)
