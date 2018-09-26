#!/usr/bin/env python
# _*_coding:utf-8_*_

import socket

sk = socket.socket()
ip_port = ('127.0.0.1', 9999)
sk.bind(ip_port)
sk.listen(5)
conn, address = sk.accept()
conn.send('hello'.encode())
conn.close()
