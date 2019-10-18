import socketserver
import sys

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address[0])
        sock = self.request

        rbuff = 'abc'

        while len(rbuff) > 0:
            rbuff = input().encode(encoding='utf-8')
            if rbuff == 'q':
                break
            sock.send(rbuff)
            print('송신 : {0}'.format(rbuff))
        sock.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('{0} <Bind IP>'.format(sys.argv[0]))
        sys.exit()

    bindIP = sys.argv[1]
    bindPort = 5425

    server = socketserver.TCPServer((bindIP, bindPort), MyTCPHandler)

    print('서버 시작..')

    server.serve_forever()