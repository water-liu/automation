#!/usr/bin/env python
# _*_coding:utf-8_*_
# 同步锁

import threading
import time


def foo():
    global num1
    # num1 -= 1
    lock.acquire()
    temp = num1
    time.sleep(0.001)
    num1 = temp - 1
    lock.release()


lock = threading.Lock()
num1 = 100
list1 = []
for i in range(100):
    t = threading.Thread(target=foo)
    t.start()
    list1.append(t)

for t in list1:
    t.join()

print(num1)
