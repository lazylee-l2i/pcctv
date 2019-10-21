import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
import socket


class Thread(QThread):
    # 시그널은 무조건 클래스 속성으로 정의해줘야 한다.
    chagned_text = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)
        self.message = ' '

        # 서버로 연결 작업
        try:
            self.sock = socket.socket(socket.AF_INET,
                                      socket.SOCK_STREAM)
            self.sock.bind(('localhost', 0))
            self.sock.connect(('localhost', 5425))
        except:
            print("IP주소가 존재하지 않거나 잘못된 경로입니다.")
            sys.exit()

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            # 무한히 받는 작업 코드를 작성
            try:
                message = self.sock.recv(1024)
                message = str(message, encoding='utf-8')
                self.message = message
            finally:
                # 특정 문자인 q 가 들어오면 작업을 종료
                if self.message == 'q':
                    self.sock.close()
                    sys.exit()
                # 그렇지 않으면 emit을 통해 슬롯으로 연결
                else:
                    self.chagned_text.emit(self.message)

if __name__ == "__main__":
    class Mywin(QWidget):
        def __init__(self):
            super().__init__()

            self.btn = QPushButton('여기를 눌러보시오', self)
            self.btn.resize(self.btn.sizeHint())
            self.btn.setToolTip('한번 만들어 보았습니다.<b>안녕하세요.<b/>')
            self.btn.move(20, 30)
            self.label = QLabel('테스트', self)
            self.setGeometry(300, 300, 400, 500)
            self.setWindowTitle('PCCTC!!S')

            # 위에서 정의해 놓은 스레드 클래스를 선언 및 실행
            self.th = Thread()
            self.th.start()

            # 슬롯으로 연결(connect)해놓으면 스레드가 돌면서
            # 데이터를 검사하며 정의 해놓은 작업을 수행함
            self.th.chagned_text.connect(self.recive_message_signal)

        # 슬롯 코드
        @pyqtSlot(str)
        def recive_message_signal(self, _text):
            # --- To Do ---
            self.label.setText(_text)

    app = QApplication(sys.argv)
    w = Mywin()
    w.show()
    sys.exit(app.exec_())
