# -*- coding:utf-8 -*-
# @Time: 2020/4/27 16:29
# @Author: assasin
# @Email: assasin0308@sina.com

# pip install redis
import redis
# from db_config import REDIS_DB


class RedisHelper(object):

    def __init__(self,redis_conn):
        self.__redis = redis.StrictRedis(
            host=redis_conn.get('host'),
            port=redis_conn.get('port'),
            db=0,
            password=None
        )

    def set(self,key,value):
        self.__redis.set(key,value)


    def get(self,key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return ""

    """......此处省略一万个方法"""


# redis_conn = RedisHelper(REDIS_DB)
# redis_conn.set('name','assasin')