#!/usr/bin/env python
# _*_coding:utf-8_*_


# from file import demo
#
# print('index', __name__)
# demo.kc()
#
# print(__file__)
# print(__doc__)


# def login(username):
#     if username == 'alex':
#         return '登录成功'
#     else:
#         return 'failed'
#
#
# def detail(username):
#     print(username, 'hello')
#
#
# user = input('please input your name:')
# if __name__ == '__main__':
#     # 检查用户是否合法
#     res = login(user)
#     if res == '登录成功':
#         # 显示详细信息
#         detail(user)
#     else:
#         print('denglushibai')
# else:
#     exit(0)


# def work(name, action='砍柴'):
#     print(name, 'go', action)
#
#
# work('ly', 'gan')
# work('hh', 'bb')


# def show(*args):
#     for item in args:
#         print(item)
#
#
# show('liuy', 'yang', 'are', 'your', 'father')
#
#
# def show2(**kwargs):
#     for item in kwargs:
#         print(item)
#
#
# show2(name='liu', age='23', job='it')

# print(range(10))

# def foo():
#     yield 1
#     yield 2
#     yield 3
#
#
# re = foo()
# for item in re:
#     print(item)


# def readlines():
#     seek = 0
#     while True:
#         with open('D:/tem.txt', 'r', encoding='utf-8') as f:
#             f.seek(seek)
#             data = f.readline()
#             if data:
#                 seek = f.tell()
#                 yield data
#             else:
#                 return
#
#
# for item in readlines():
#     print(item)

#
# result = 'gt' if 1 > 3 else 'lt'
# print(result)

# a = []
# # print(help(a))
# print(type(a))

# t1 = 123
# t2 = 124
# print(id(t1))
# print(id(t2))
#
# print(max([11, 22, 33, 44, 666]))
# print(sum([11, 22, 33, 44, 666]))
# print(pow(2, 11))

# print(chr(65))
# print(ord('A'))

# s = 'i am {0},you are {1}'
# print(s.format('23', 'ds'))
# site = {'name': 'aa', 'url': 'wwww'}
# print('网站名称：{name}, 地址: {url}'.format(**site))

# temp = map(lambda x, y: x+y, [1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
# for i in temp:
#     print(i)
# print(list(temp))

# a = '8*8'
# print(eval(a))
# 反射:通过字符串的模式导入模块。


# '''
# temp = 'sys'
# model = __import__(temp)
# print(model.path)
# '''

# 大型网站，用于切换数据库连接
# temp = 'mysqlserver'
# func = 'count'
# model = __import__(temp)
# Function = getattr(model, func)

# import random


# print(random.randint(1, 10))
# # 大于等于1，小于等于10
#
# print(random.randrange(1, 10))
# # 大于等于1， 小于10
#
# print(chr(random.randint(65, 90)))

# # 生产验证码
# code = []
# for i in range(6):
#     if i == random.randint(1, 9):
#         # print(random.randint(1, 9))
#         code.append(str(random.randint(1, 9)))
#     else:
#         temp = random.randint(65, 90)
#         # print(chr(temp))
#         code.append(chr(temp))
# print(''.join(code))
# # 转为字符串

# import hashlib
#
# hash = hashlib.md5('admin')

# import pickle
# python与Python之间数据传输序列化

# li = ['alex', 22, 11, 'ok']
# print(pickle.dumps(li))
# print(type(pickle.dumps(li)))

# f = open('D:/text.txt', 'wb')
# f.write(pickle.dumps(li))
# f.close()
#
# f1 = open('D:/text.txt', 'rb')
# data = pickle.loads(f1.read())
# print(data)

# f2 = open('D:/text2.txt', 'wb')
# pickle.dump(li, f2)
#
# f2 = open('D:/text2.txt', 'rb')
# red = pickle.load(f2)
# print(red)


# import re


# result1 = re.match('\d+', '123akdjf2345')
# print(result1)
# result2 = re.search('\d+', 'adfc234ds235')
# print(result2)
# print(result2.group())
# result3 = re.findall('\d+', 'asdfj234lakjdf334')
# print(result3)
# com = re.compile('\d+')
# print(com.findall('adsf234adsf567'))

# result2 = re.search('(\d+)[a-z]*(\d+)', 'akdlsjfa234adskfj45553')
# print(result2.group())
# print(result2.groups())


# import time
#
#
# print(time.time())
# print(time.gmtime())
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
