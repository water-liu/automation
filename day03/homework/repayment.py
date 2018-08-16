#!/usr/bin/env python
# _*_coding:utf-8_*_
Alice = ['Alice', 15000, 10000]
Beth = ['Beth', 15000]
Cecil = ['Cecil', 12000]
Den = ['Den', 12000]


def judge_name(username):
    if username == Alice[0]:
        return Alice
    elif username == Beth[0]:
        return Beth
    elif username == Cecil[0]:
        return Cecil
    else:
        return Den


# 查询
def query(username):
    list1 = judge_name(username)
    return list1[-1]


# 固定额度fixed credit
# 可用额度available credit
# 还款
def repayment(username, repay):
    list1 = judge_name(username)
    num = list1[-1]
    judge_name(username).append(list1[-1]+repay)
    if judge_name(username)[-1] > num:
        return True
    else:
        return False


def operation(username):
    while True:
        while True:
            available = query(username)
            fixed = judge_name(username)[1]
            if available >= fixed:
                print("账单您已经还清！")
                break
            print('你需要还款%s元，' % (fixed - available))
            repay = int(input('请输入你的还款金额(退出请输入0)：'))
            if int(repay) >= 1:
                s = repayment(username, repay)
                if s:
                    print('还款%s元成功\n' % repay)
                else:
                    print('还款失败')
            elif 0 < int(repay) < 1:
                print('还款至少1元')
            elif int(repay) == 0:
                break
            else:
                print('请输入正确的还款金额！')

        logout = input("是否退出？[yes/no]:")
        if logout == 'yes':
            break
        elif logout == 'no':
            continue
        else:
            break



