from flask import Blueprint

Edit_Doc = Blueprint('Edit_Doc', __name__, url_prefix='/api/doc')

from apps.Edit_Doc.controller.edit import *
