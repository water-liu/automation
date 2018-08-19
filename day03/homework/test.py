#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:liuyang
@file: test.py
@time: 2018/08/{DAY}
"""
import os
import time
import pickle


dict1 = {
    '1': '取现',
    '2': '还款',
    '3': '查询',
    '4': '转账',
    '5': '商城',
    '6': '退出',
}
# datetime = time.time()
# dict2 = {
#     1: {'name': 'Alice', '消费类型': '商城', '消费金额': 300, '手续费': 0, '消费时间': time.strftime('%Y-%m-%d %H:%M:%S')}
# }
#
#
# f = open('record.txt', 'ab')
# pickle.dump(dict1, f)
# pickle.dump(dict2, f)
# f.close()
#
# # f1 = open('record.txt', 'rb')
# print(pickle.loads('record.txt'))
# # print(pickle.load(f1))

# test = 123
# test = -test
# print(type(test))


f = open('credit.txt', 'w')

# while True:
#     listname = f1.readline().split(',')
#     print(type(listname))
#     print(listname)
#     print(listname[0])
#     if listname[0] == 'Alice':
#         print('True')
#     break
# f1.close()
# print(listname)
