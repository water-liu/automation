#!/usr/bin/env python
# _*_coding:utf-8_*_

import queue


# q = queue.Queue()
# q.put(12)
# q.put("liu")
# q.put({"name": "aa"})
#
# while 1:
#     data = q.get()
#     print(data)
#     print("-------")

q = queue.LifoQueue()
q.put(12)
q.put("liu")
q.put({"name": "aa"})

while 1:
    data = q.get()
    print(data)
    print("------")

