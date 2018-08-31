#!/usr/bin/env python
# _*_coding:utf-8_*_
from day5.model.admin import Admin


def main():
    user = input('username:')
    passwd = input('password:')
    admin = Admin()
    result = admin.checkvalidate(user, passwd)
    if not result:
        print('登录失败')
    else:
        print('登录成功')


if __name__ == '__main__':
    main()
