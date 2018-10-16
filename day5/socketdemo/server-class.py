#!/usr/bin/env python
# _*_coding:utf-8_*_

import socketserver


class Myserver(socketserver.BaseRequestHandler):

    def setup(self):
        pass

    def handle(self):
        conn = self.request
        conn.send('hello.'.encode())
        flag = True
        while flag:
            data = conn.recv(1024)
            print(data)
            if data == 'exit':
                flag = False
            conn.send('ss'.encode())
        conn.close()

    def finish(self):
        pass


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), Myserver)
    server.serve_forever()


