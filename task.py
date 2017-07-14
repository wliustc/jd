#!/usr/bin/python
# -*- coding: utf-8 -*-

# 1. sign
# 2. get the regular coupon
# 3. check the good coupon
# 4. push to the wechat
# 5. for many users

from account import Account
from miscellaneous import *

class Task:
    def __init__(self):
        self.users = self.get_users()
        self.task_cnt = 0

    def get_users(self):
        users = {}
        with open('user.dat', 'r') as f:
            for line in f:
                if line.strip():
                    u, p = line.strip().split(':')
                    users[u] = p
        print_([u for u in users])
        return users
    
    def data_sign(self, account):
        try:
            account.m_data_sign()
        finally:
            account.quit()
            
    def charge_coupon(self, account):
        try:
            account.m_charge_coupon()
        finally:
            account.quit()

    def do(self, func, users = []):
        user_cnt = 0
        for u, p in self.users.items():
            if not users or u in users:
                print_('\n\n############ Task %d [%s] User %d [%s] ############\n' % (self.task_cnt, func.__name__, user_cnt, u))
                acc = Account(u, p)
                func(acc)
                user_cnt += 1
        self.task_cnt += 1

if __name__ == '__main__':
    task = Task()
    # 13917053319, jdcarol0701, jd_5f3fd86191c95
    #task.do(task.data_sign)
    #task.do(task.data_sign, ['jdcarol0701', 'jd_5f3fd86191c95'])
    task.do(task.charge_coupon, ['13917053319'])


        