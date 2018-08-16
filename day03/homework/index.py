#!/usr/bin/env python
# _*_coding:utf-8_*_
import repayment


# 登录
def login(username, passwd):
    pass_table = {
        'Alice': '123456',
        'Beth': '123456',
        'Cecil': '123456',
        'Den': '123456'
    }
    if username in pass_table.keys():
        if pass_table[username] == passwd:
            return 1
        else:
            return 2
    else:
        return 3




# 转账
def transfer():
    pass


string_home = '''
    网银系统欢迎您： 
        1. 取现
        2. 还款
        3. 查询
        4. 转账
        5. 商城
        6. 退出
    请选择您的业务： 
'''
dict_home = {
    '1': '取现',
    '2': '还款',
    '3': '查询',
    '4': '转账',
    '5': '商城',
    '6': '退出'
}


def main():
    # 登录判断
    while True:
        print('welcome you come !')
        username = input('please input your username:')
        passwd = input('please input your password:')
        if login(username, passwd) == 1:
            break
        elif login(username, passwd) == 2:
            print("密码输入错误")
        elif login(username, passwd) == 3:
            print("用户不存在！")
        else:
            print('系统有误，请重新登录')
    while True:
        print(string_home)
        choose = input('请选择你需要的业务，输入对应的序号即可：')
        if choose in dict_home.keys():
            if int(choose) == 1:
                withdrawal()
            elif int(choose) == 2:
                repayment.operation(username)
            elif int(choose) == 3:
                pass
            elif int(choose) == 4:
                pass
            elif int(choose) == 5:
                pass
            elif int(choose) == 6:
                pass
                break
        else:
            print('您的选择不正确，请再次选择')


if __name__ == '__main__':
    main()

# 思路: 交易记录写入文件，可以用pickle序列化，用ID区别不同的人 ， 后面用字典存记录
# 额度，由列表从文件中读取，退出登录时，需要把列表再写入文件，下次登录时读取。
