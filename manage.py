import flask
from apps.AllController import create_app

from gevent import monkey
from gevent.pywsgi import WSGIServer
monkey.patch_all()

app = create_app('Dev')

if __name__ == '__main__':
    app.run(debug=True)