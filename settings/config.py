import redis


class BaseConfig(object):
    def __init__(self, *args, **kwargs):
        SECRET_KEY = 'wenchao1026'
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        SQLALCHEMY_RECORD_QUERIES = True

        # sessioin配置
        SESSION_TYPE = "redis"  # 指定session的保存位置
        SESSION_USE_SIGNER = True  # 设置sessioin存储签名
        SESSION_REDIS = redis.StrictRedis(host='127.0.0.1', port=6379)
        PERMANENT_SESSION_LIFETIME = 24 * 3600 * 2  # session的有效时间,单位秒


class DevConfig(object):
    def __init__(self):
     super(BaseConfig, self).__init__()
     DEBUG = False
     SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@localhost:3306/zhuge_dm'


config = {
    'Dev': DevConfig,
}