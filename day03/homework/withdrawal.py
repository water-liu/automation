#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:liuyang
@file: withdrawal.py
@time: 2018/08/{DAY}
"""
import time
import recordoperation
import repayment


# 取现
def withdrawal(username, consumetyep, money, services):
    # 获取可取现金额
    avamoney = repayment.query(username)
    updatetime = time.strftime('%Y-%m-%d %H:%M:%S')
    if services < 5:
        services = 5
    # 写入交易记录
    request = recordoperation.write_record(username, consumetyep, money, services, updatetime)
    # 计算取现金额和服务费
    consume_money = money + services
    request1 = repayment.updatelist(username, -consume_money)
    if request and request1 < avamoney:
        return True
    else:
        return False


def maincrash(username):
    while True:
        avamoney = repayment.query(username)
        print('您的可取现额度为%s元，取现需要收取手续费百分之五,手续费最低5元' % avamoney)
        print('注意：输入0为退出！')
        money = int(input('请输入你需要取现的金额：'))
        if 0 < money <= avamoney:
            services = money*0.05
            if services < 5:
                services = 5
            request = withdrawal(username, '取现', money, services)
            withmoney = money + services
            request2 = repayment.updatelist(username, -withmoney)
            if request and request2:
                print('取现成功！')
            else:
                print('取现失败！请返回查看交易记录')
        elif money == 0:
            break
        elif money > avamoney:
            print('你的余额不足！')
        else:
            print('输入的金额有误！请重新输入！')

