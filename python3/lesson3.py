#!/usr/bin/env python
# _*_coding:utf-8_*_
# 死锁
import threading
import time


class MyThread(threading.Thread):

    def actiona(self):
        r_lock.acquire()
        print("gotA线程名称: ", self.name, time.ctime())
        time.sleep(2)
        r_lock.acquire()
        print("gotB线程名称: ", self.name, time.ctime())
        time.sleep(1)
        r_lock.release()
        r_lock.release()

    def actionb(self):
        r_lock.acquire()
        print("gotB线程名称: ", self.name, time.ctime())
        time.sleep(2)
        r_lock.acquire()
        print("gotA线程名称: ", self.name, time.ctime())
        time.sleep(1)
        r_lock.release()
        r_lock.release()

    def run(self):
        self.actiona()
        self.actionb()


if __name__ == '__main__':

    A = threading.Lock()
    B = threading.Lock()
    r_lock = threading.RLock()
    list1 = []

    for i in range(5):
        t = MyThread()
        t.start()
        list1.append(t)

    for t in list1:
        t.join()
