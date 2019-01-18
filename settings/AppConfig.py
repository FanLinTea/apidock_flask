from flask import Flask,Response
from settings.BaseConfig import config
from flask_session import Session
from werkzeug.datastructures import Headers

session = Session()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    #  修改response 的 响应头,来解决跨域问题
    app.response_class = NewResponse

    session.init_app(app)

    from apps.Edit_Doc.Edit_Doc_Blueprint import Edit_Doc
    from apps.InternalPage.internalPage_Blueprint import internalpage
    app.register_blueprint(Edit_Doc)
    app.register_blueprint(internalpage)

    return app


class NewResponse(Response):
    '''解决跨域请求'''
    def __init__(self, response=None, **kwargs):
        kwargs['headers'] = ''
        headers = kwargs.get('headers')
        # 跨域控制
        origin = ('Access-Control-Allow-Origin', '*')
        methods = ('Access-Control-Allow-Methods', 'HEAD, OPTIONS, GET, POST, DELETE, PUT')
        if headers:
            headers.add(*origin)
            headers.add(*methods)
        else:
            headers = Headers([origin, methods])
        kwargs['headers'] = headers
        return super().__init__(response, **kwargs)