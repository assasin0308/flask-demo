# pip install redis
import redis
# from db_config import REDIS_DB


class RedisHelper(object):

    def __init__(self,redis_conn):
        self.__redis = redis.StrictRedis(
            host=redis_conn.get('host'),
            port=redis_conn.get('port')
        )

    def set(self,key,value):
        self.__redis.set(key,value)


    def get(self,key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return ""


# redis_conn = RedisHelper(REDIS_DB)
# redis_conn.set('name','assasin')