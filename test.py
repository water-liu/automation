#!/usr/bin/env python
# _*_coding:utf-8_*_

print("liuy")

name = input('please input your name :')
age = int(input('please input your age:'))
work = input('please input your job：')
salary = input('please input your salary:')

if age > 30:
    print("you are very too old")
elif age > 20:
    print("you are young")
else:
    print("you are very young")

print('''
    Personal information of %s:
        name: %s
        age : %s
        work: %s
        salary: %s
        
''' % (name, name, age, work, salary))
