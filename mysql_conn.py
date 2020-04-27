import pymysql
pymysql.install_as_MySQLdb()
# from db_config import MYSQL_DB_DEFAULT


# 单例模式 MySQL数据库连接
class MysqlConn(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self,db_conn_params):
        self.db_host = db_conn_params.get('host')
        self.db_port = db_conn_params.get('port')
        self.db_user = db_conn_params.get('user')
        self.db_passwd = db_conn_params.get('password')
        self.db_name = db_conn_params.get('db_name')
        self.db_charset = db_conn_params.get('db_charset')

        try:
            self.connection = pymysql.connect(
                host=self.db_host,
                port=self.db_port,
                user=self.db_user,
                password=self.db_passwd,
                db=self.db_name,
                charset=self.db_charset
            )
            if self.connection.open:
                self.cursor = self.connection.cursor()
        except Exception as conn_error:
            print(conn_error)

     # fetchall
    def select(self,sql):
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            self.connection.commit()
            self.close()
            return result
        except:
            self.connection.rollback()
            self.close()

    # fetchone
    def row(self,sql):
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            self.connection.commit()
            self.close()
            return result
        except :
            self.connection.commit()
            self.close()

    # update
    def update(self,sql):
        try:
            affect_rows = self.cursor.execute(sql)
            self.connection.commit()
            self.close()
            return affect_rows
        except:
            self.connection.rollback()
            self.close()

    # delete
    def delete(self,sql):
        try:
            affect_rows = self.cursor.execute(sql)
            self.connection.commit()
            self.close()
            return affect_rows
        except :
            self.connection.rollback()
            self.close()

     # truncate table
    def truncate(self,table_name):
        self.cursor.execute(" truncate table " + table_name )
        self.connection.commit()
        self.close()


    # close connection
    def close(self):
        self.cursor.close()
        self.connection.close()

# conn1 = MysqlConn(MYSQL_DB_DEFAULT)
# result = conn1.select(" select * from users  ")
# print(result)