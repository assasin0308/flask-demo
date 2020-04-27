# -*- coding:utf-8 -*-
# @Time: 2020/4/27 16:29
# @Author: assasin
# @Email: assasin0308@sina.com
# @File: ssdb_conn.py

import os,sys
from sys import stdin,stdout

from SSDB import SSDB

class SSDBHelper(object):

    def __init__(self):
        try:
            self.ssdb = SSDB('127.0.0.1', 8888)
        except Exception as e:
            print(e)
            sys.exit(0)

    def  set(self,key,value):
        self.ssdb.request('set',[key,value])

    def get(self,key):
        self.ssdb.request('get',[key])

    def incr(self,key,incr_num):
        self.ssdb.request('incr',[key,incr_num])

    def decr(self,key,decr_num):
        self.ssdb.request('decr',[key,decr_num])

    def delete(self,key):
        self.ssdb.request('del',[key])

    """......此处省略一万个方法"""

