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
temp = 'mysqlserver'
func = 'count'
model = __import__(temp)
Function = getattr(model, func)
