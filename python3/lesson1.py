#!/usr/bin/env python
# _*_coding:utf-8_*_
import threading
import time


def add():
    sum1 = 0
    for i in range(100000):
        sum1 += i
    print(sum1)


def mul():
    sum2 = 1
    for n in range(1, 100000):
        sum2 *= n
    print(sum2)


start = time.time()
t1 = threading.Thread(target=add)
t2 = threading.Thread(target=mul)

l = [t1, t2]

for t in l:
    t.start()

for a in l:
    a.join()

print("cost time %s" % (time.time() - start))
