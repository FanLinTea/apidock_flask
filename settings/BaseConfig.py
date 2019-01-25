import redis
from DBUtils.PooledDB import PooledDB
from settings.db_config import Mysql
import threadpool
import pymysql
from settings import db_config


class BaseConfig(object):
    def __init__(self, *args, **kwargs):
        SECRET_KEY = 'zhuge_dm'
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        SQLALCHEMY_RECORD_QUERIES = True

        # sessioin配置
        SESSION_TYPE = "redis"  # 指定session的保存位置
        SESSION_USE_SIGNER = True  # 设置sessioin存储签名
        PERMANENT_SESSION_LIFETIME = 24 * 3600 * 2  # session的有效时间,单位秒


class DevConfig(BaseConfig):
    def __init__(self, *args, **kwargs):
        pass


class ProdConfig(BaseConfig):
    def __init__(self, *args, **kwargs):
        pass


config = {
    'dev': DevConfig,
    'prod': ProdConfig
}

mysql_pool = {}
for db_name, mysql_con in Mysql.items():
    try:
        pool = PooledDB(pymysql, 5, host=mysql_con.get('host'), user=mysql_con.get('user'),
                        passwd=mysql_con.get('password'), port=mysql_con.get('port'), charset="utf8")
    except Exception as e:
        print('数据库配置出错', e)
    mysql_pool[db_name] = pool
print(mysql_pool)


class Connect_mysql(object):
    '''
    使用mysql连接池  以及  线程池 执行sql语句
    实例化类的时候  输入想要连接的数据库
    只需要调取 thread_sql 方法  注意参数是列表
    '''
    _mysql_config = db_config.Mysql

    def __init__(self, mysql_name):
        self.mysql = Connect_mysql._mysql_config.get(mysql_name)
        if not self.mysql:
            raise Exception('你输入的数据库别名有误,或者你数据库未配置')
        #  连接池
        try:
            self.pool = mysql_pool.get(mysql_name)
        except Exception as e:
            print(e)

        #  线程池
        self.thread_poll = threadpool.ThreadPool(5)
        self.mysql_data = []

    def select_sql(self, sql=''):
        conn = self.pool.connection()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            # print('查询出的数据是: ', data)
            cursor.close()
            self.mysql_data.append(data)
            # a = 1/0
            # print(a)
            return data
        except Exception as e:
            print(e)

        finally:
            cursor.close()
            conn.close()

    def other_sql(self, sql=''):
        conn = self.pool.connection()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            cursor.execute(sql)
            info = cursor.rowcount
            if info:
                self.mysql_data.append(info)
                # print('操作数据库成功')
            else:
                print('数据库操作失败', sql)
                # print('数据库操作失败')
                # print(sql)
            conn.commit()
            return info
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def thread_sql(self, sqls):
        self.mysql_data = []
        '''线程池启动'''
        if not isinstance(sqls, list):
            raise Exception('请把需要执行的所有 sql 语句放入列表中,即使是单条sql语句,这样才能给线程池传参')
        if 'select' in sqls[0]:
            request = threadpool.makeRequests(self.select_sql, sqls)
            for req in request:
                self.thread_poll.putRequest(req)
            self.thread_poll.wait()
            return self.mysql_data
        else:
            request = threadpool.makeRequests(self.other_sql, sqls)
            for req in request:
                self.thread_poll.putRequest(req)
            self.thread_poll.wait()
            return self.mysql_data
