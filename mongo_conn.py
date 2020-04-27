# -*- coding:utf-8 -*-
# @Time: 2020/4/27 16:29
# @Author: assasin
# @Email: assasin0308@sina.com

# pip install pymongo
# 无安全认证
# client = MongoClient('mongodb://localhost:27017')
# 有安全认证
# client = MongoClient('mongodb://用户名:密码@localhost:27017/数据库名称')

from pymongo import *

class MongodbConn(object):
    def __init__(self,mongo_conn_params):
        mongo_auth_user = mongo_conn_params.get('user','')
        mongo_auth_passwd = mongo_conn_params.get('password','')
        mongo_db_name =  mongo_conn_params.get('db_name','')
        if not all([mongo_auth_user,mongo_auth_passwd]):
            self.client = MongoClient("mongodb://" + mongo_conn_params.get('host') + ':' + mongo_conn_params.get('port'))
        else:
            self.client = MongoClient("mongodb://" + mongo_auth_user + ':' + mongo_auth_passwd + '@'
                                      +  mongo_conn_params.get('host') + ':' + mongo_conn_params.get('port') + '/' + mongo_db_name )

    """......此处省略一万个方法"""


# 获取客户端,建立连接
# client = MongoClient('mongodb://127.0.0.1:27017')
# 切换数据库
# db = client.py3
# 获取集合
# stu = db.stu
# 添加一条数据
# stu.insert_one({'name':'张三丰'})
# 修改
# stu.update_one({'name':'张三丰'},{'$set':{'name':'史斌'}})
# 删除
# stu.delete_one({'name':'assasin'})
# 查询
# cursor = stu.find({'age':{'$gt':20}})
# cursor = stu.find({'age':{'$gt':20}}).sort('age',ASCENDING) # DESCENDING:降序|ASCENDING:升序
# for s in cursor:
#     print(s['name'])