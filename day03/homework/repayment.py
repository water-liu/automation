#!/usr/bin/env python
# _*_coding:utf-8_*_
# Alice = ['Alice', 15000, 10000]
# Beth = ['Beth', 15000]
# Cecil = ['Cecil', 12000]
# Den = ['Den', 12000]


def read_list(username):
    f1 = open('credit.txt', 'r')
    while True:
        listname = f1.readline()
        if list(listname)[0] == username:
            break
    f1.close()
    return list(listname)


listgo = read_list('Alice')
print(listgo)


def write_list(username, listre):
    with open('credit.txt', 'r') as f:
        lines = f.readlines()
    with open('credit.txt', 'w') as f_w:
        for linen in lines:
            if username in linen:
                break
        f_w.write(listre)
    f_w.close()
    return True
# def judge_name(username):
#     listh = read_list()
#     if username == listh[0][0]:
#         return listh[0]
#     elif username == listh[1][0]:
#         return listh[1]
#     elif username == listh[2][0]:
#         return listh[2]
#     else:
#         return listh[3]


# 查询
def query(username):
    list1 = read_list(username)
    return list1[-1]


# 更改额度列表
def updatelist(username, money):
    list1 = read_list(username)
    list2 = read_list(username).append(list1[-1] + money)
    request = write_list(username, list2)
    if request:
        return True
    else:
        return False


# 固定额度fixed credit
# 可用额度available credit
# 还款
def repayment(username, repay, available):
    request = updatelist(username, repay)
    if request:
        num = read_list(username)[-1]
        if num > available:
            return True
        else:
            return False
    else:
        return False


def operation(username):
    while True:
        while True:
            available = query(username)
            fixed = read_list(username)[1]
            if available >= fixed:
                print("账单您已经还清！")
                break
            print('你需要还款%s元，' % (fixed - available))
            repay = int(input('请输入你的还款金额(退出请输入0)：'))
            if int(repay) >= 1:
                s = repayment(username, repay, available)
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



