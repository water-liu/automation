#!/usr/bin/env python
# _*_coding:utf-8_*_
# 模板 == 类


class Person:

    def __init__(self, name, gene, weight):
        self.Name = name
        self.__Gene = gene
        if name != 'alex':
            self.Gender = 'men'
        self.Weight = weight
        self.Age = None

    @property
    def talk(self):
        print('xxxxx')

    def fight(self, weight):
        if self.Weight > weight:
            print('fight')
        else:
            print('run')


p1 = Person('n1', 'a', 190)
p1.Age = 18
