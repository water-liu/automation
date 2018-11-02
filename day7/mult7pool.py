#!/usr/bin/env python
# _*_coding:utf-8_*_

from multiprocessing import Pool
import time


def f(x):
    print(x*x)
    time.sleep(1)
    return x*x


poolredis = Pool(processes=4)
res_list = []
for i in range(10):
    res = poolredis.apply_async(f, [i, ])
    res_list.append(res)

for i in res_list:
    print(i)

