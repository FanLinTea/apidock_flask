from settings.AppConfig import create_app
from settings.db_config import Mysql, Online_Mysql
# from gevent import monkey

# monkey.patch_all()


app = create_app('prod')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)