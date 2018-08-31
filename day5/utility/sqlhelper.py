#!/usr/bin/env python
# _*_coding:utf-8_*_
import pymysql
from day5 import conf

class MySqlHelper:

    def __init__(self):
        self.__conn_dict = conf.conn_string

    def get_dict(self, sql, params):
        connection = pymysql.connect(**self.__conn_dict)
        cursor = connection.cursor()
        cursor.execute(sql, params)
        data = cursor.fetchall()
        cursor.close()
        connection.close()
        return data

    def get_one(self, sql, params):
        connection = pymysql.connect(**self.__conn_dict)
        cursor = connection.cursor()
        cursor.execute(sql, params)
        data = cursor.fetchone()
        cursor.close()
        connection.close()
        return data

