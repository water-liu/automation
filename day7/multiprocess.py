#!/usr/bin/env python
# _*_coding:utf-8_*_

from multiprocessing import Process, Queue


def f(queue, n):
    queue.put([n, 'hello'])


if __name__ == '__main__':
    q = Queue()
    for i in range(5):
        p = Process(target=f, args=(q, i))
        p.start()
    print(q.get())
