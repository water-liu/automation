#!/usr/bin/env python
# _*_coding:utf-8_*_

# str1 = 'demo'
# str2 = 'foo'
#
# module = __import__()


# class Alex:
#     xx = '没心没肺'
#
#
# class Person:
#     xue = 'xue'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# p1 = Person('liyang', 18)
# print(p1.name)
# p2 = Person('laoda', 16)
# print(p1.age)


# class Province:
#     # 静态字段
#     memo = 'hhhhh'
#
#     def __init__(self, name, capital, leader, thailand):
#         # 动态字段
#         self.Name = name
#         self.Capital = capital
#         self.Leader = leader
#         self.__thailand = thailand
#
#     # 动态方法
#     def sports_meet(self):
#         print(self.Name + 'sporting')
#
#     # 静态方法
#     @staticmethod
#     def fanfu():
#         print('fanfu is jinxingzhong')
#
#     # 特性方法
#     @property
#     def bar(self):
#         # print(self.Leader)
#         return 'haha'
#
#     @property
#     def thailand(self):
#         return self.__thailand
#
#     @thailand.setter
#     def thailand(self, value):
#         self.__thailand = value
#
#
#     # def thailand(self, value):
#     #     self.__thailand = value
#
#
# # hebei = Province('hebei', 'shijiazhuang', 'liyang')
# # shandong = Province('shandong', 'jinan', 'wang')
# # print(hebei.Capital)
# # print(Province.memo)
# # print(hebei.memo)
# # hebei.sports_meet()
# # Province.fanfu()
# # hebei.fanfu()
# # print(hebei.bar)
#
# japan = Province('aa', 'bb', 'cc', True)
# print(japan.thailand)
# Province.thailand = False
# print(japan.thailand)


# from abc import ABCMeta
# from abc import abstractmethod
#
#
# class Bar:
#     __metaclass__ = ABCMeta
#
#     @abstractmethod
#     def send(self):
#         pass
#
#
# class Alert(Bar):
#     def __init__(self):
#         print('init')
#
#     def send(self):
#         print('send')


# f = Alert()
# f
# f.send()
#
# class MyException(Exception):
#     def __init__(self, msg):
#         self.error = msg
#
#     def __str__(self, *args, **kwargs):
#         return self.error
#
#
# obj = MyException('error and fail')
# print(obj)
# raise MyException('zidingyi')

def validate(name, pwd):
    if name == 'aa' and pwd == '123456':
        return True
    else:
        return False


res = validate('aa', '123456')
try:
    if res:
        print('登录成功')
    else:
        raise
except e:
    print('cuowu')
    print('denglushibei')