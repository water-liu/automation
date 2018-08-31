#!/usr/bin/env python
# _*_coding:utf-8_*_

# request = 'gt' if 1 < 3 else 'lt'
# print(request)
# import pymysql

# cursor = connection.cursor()
# sql1 = "insert into userinfo(id,name) values(%s, %s)"
# cursor.execute(sql1, (5, 'ee'))
# connection.commit()
#
# sql = 'select * from userinfo'
# data = cursor.execute(sql)
# data2 = cursor.fetchall()
# connection.close()
#
# print(data)
# print(data2)
# import pymysql
#
#
# connection = pymysql.connect(host='192.168.1.207', user='liuy', password='liuy123', db='08day5')
# cursor = connection.cursor()
# sql = "insert into admin(name, address) values(%s, %s)"
# params = ('andy', 'beijing')
# params2 = [('andy', 'beijing'), ('ff', 'guangzhou'), ('gg', 'hunan'), ('hh', 'hongkong')]
# # reCount = cursor.execute(sql, params)
# recount2 = cursor.executemany(sql, params2)
# # 执行多条语句用execcutemany
# connection.commit()
# connection.close()
# print(recount2)


'''
执行事务
事务机制可以确保数据一致性。

事务应该具有4个属性：原子性、一致性、隔离性、持久性。这四个属性通常称为ACID特性。

原子性（atomicity）。一个事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做。
一致性（consistency）。事务必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的。
隔离性（isolation）。一个事务的执行不能被其他事务干扰。即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。
持久性（durability）。持续性也称永久性（permanence），指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。接下来的其他操作或故障不应该对其有任何影响。

'''

connection = pymysql.connect(host='192.168.1.207', user='liuy', password='liuy123', db='08day5')

# Django里面事务就是放在装饰器里面
# cursor = connection.cursor()
# cursor.execute('select * from admin')
# data = cursor.fetchone()
# print(data)
# data1 = cursor.fetchone()
# print(data1)
# data2 = cursor.fetchone()
# print(data2)
# cursor.scroll(-1, mode='relative')
# data3 = cursor.fetchone()
# print(data3)
# cursor.scroll(5, mode='absolute')
# data4 = cursor.fetchone()
# print(data4)
# # 输出绝对位置的数据
# # cursor.scroll(0, mode='absolute')
# # 输出相对上一条位置移动后的数据
# # cursor.scroll(-1, mode='relative')
# connection.close()
# cursor = connection.cursor()
# sql = "insert into admin(name, address) values(%s, %s)"
# params = ('dd', 'gansu3')
# cursor.execute(sql, params)
# connection.commit()
# last_id = cursor.lastrowid
# new_id = connection.insert_id()
# print(last_id)
# print(new_id)
#
# connection.close()

