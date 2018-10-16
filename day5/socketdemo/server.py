#!/usr/bin/env python
# _*_coding:utf-8_*_

import socket

sk = socket.socket()
ip_port = ('127.0.0.1', 9999)
sk.bind(ip_port)
sk.listen(5)
while True:
    conn, address = sk.accept()
    conn.send('hello'.encode())
    flag = True
    while flag:
        data = conn.recv(1024)
        print(data)
        if data == 'exit':
            flag = False
        conn.send('ss'.encode())
    conn.close()

