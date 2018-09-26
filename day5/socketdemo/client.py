#!/usr/bin/env python
# _*_coding:utf-8_*_

import socket

client = socket.socket()
ip_port = ('127.0.0.1', 9999)
client.connect(ip_port)
data = client.recv(2048)
print(data)
