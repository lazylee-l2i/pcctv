import socketserver
import sys

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address[0])
        sock = self.request

        rbuff = 'abc'

        while len(rbuff) > 0:
            rbuff = input()
            sock.send(rbuff.encode(encoding='utf-8'))
            print('송신 : {0}'.format(rbuff))
            if rbuff == 'q':
                break
        sock.close()

if __name__ == '__main__':
    #bindIP = sys.argv[1]
    bindIP = 'localhost'
    bindPort = 5425

    server = socketserver.TCPServer((bindIP, bindPort), MyTCPHandler)

    print('서버 시작..')

    server.serve_forever()