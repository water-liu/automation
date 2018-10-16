#!/usr/bin/env python
# _*_coding:utf-8_*_

from multiprocessing import Pool
import time


def f(x):
    time.sleep(0.5)
    return x*x


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
if __name__ == '__main__':
    p = Pool(5)
    print(list(p.map(f, a)))

