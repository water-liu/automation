#!/usr/bin/env python
# _*_coding:utf-8_*_

from multiprocessing import Process
import os
import time


def info(title):
    print("title:", title)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name):
    info('function f')
    print('hello', name)


if __name__ == '__main__':
    info('main process line')
    time.sleep(1)
    print("------------------")
    p = Process(target=info, args=('yuan',))
    p.start()
    p.join()
