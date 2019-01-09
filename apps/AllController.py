from flask import Flask
from settings.config import config
from flask_session import Session

session = Session()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    session.init_app(app)

    from apps.Edit_Doc.Edit_Doc_Blueprint import Edit_Doc
    app.register_blueprint(Edit_Doc)

    return app
