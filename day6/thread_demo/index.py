#!/usr/bin/env python
# _*_coding:utf-8_*_

from threading import Thread


def foo(arg, v):
    print(arg, v)


print('before')
th1 = Thread(target=foo, args=(1, 11,))  # 创建线程
th1.start()
print('after')

