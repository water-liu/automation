#!/usr/bin/env python
# _*_coding:utf-8_*_


def outer(func):
    def wrapper():
        print('alibaba')
        func()
        print('aaaaa')
    return wrapper


@outer
def func1():
    print('func1')
# seem to  outer(func1)

# @outer
# def func2():
#     print('func2')


# @outer
# def func3():
#     print('func3')


func1()
# func2()
# func3()

