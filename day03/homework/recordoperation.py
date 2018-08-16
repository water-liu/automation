#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:liuyang
@file: recordoperation.py
@time: 2018/08/{DAY}
"""
import pickle

file = 'record.txt'
''' record.txt 格式
    每行username, consumetype, money, services, updatetime
'''


def read_record(username):
    li = []
    f = open(file, 'rb')
    for line in f:
        read = pickle.load(line)
        if read['username'] == username:
            li.append(read)
    f.close()
    return li


def write_record(username, consumetype, money, services, updatetime):
    f = open(file, 'ab')
    dict1 = {
        'username': username,
        'consumetype': consumetype,
        'money': money,
        'services': services,
        'updatetime': updatetime
    }
    pickle.dump(dict1, f)
    return True



