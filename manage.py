from settings.AppConfig import create_app

from gevent import monkey

monkey.patch_all()

app = create_app('dev')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)