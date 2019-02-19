import pymysql
from settings.db_config import Mysql


for name,data in Mysql.items():
    try:
        print(name)
        conn = pymysql.connect(
            host=data.get('host'),
            user=data.get('user'),password=data.get('password'),
            charset="utf8")
        print('链接成功??')
    except Exception as e:
        print(e)
