#!/usr/bin/env python
# _*_coding:utf-8_*_

import time
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, num):
        self.num = num

    def run(self):
        pass


def foo(j):
    time.sleep(1)
    print(p.is_alive(), j, p.pid)
    time.sleep(1)


if __name__ == '__main__':
    p_list = []
    for i in range(10):
        p = Process(target=foo, args=(i, ))
        p_list.append(p)

    for p in p_list:
        p.start()

    print('main process over!')

