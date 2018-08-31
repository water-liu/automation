#!/usr/bin/env python
# _*_coding:utf-8_*_
from day5.utility.sqlhelper import MySqlHelper


class Admin:
    def __init__(self):
        self.__helper = MySqlHelper()

    def checkvalidate(self, username, password):
        sql = "select * from admin where name=%s and address=%s"
        params = (username, password)
        return self.__helper.get_one(sql, params)
