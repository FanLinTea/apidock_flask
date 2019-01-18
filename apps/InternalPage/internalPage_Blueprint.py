from flask import Blueprint

internalpage = Blueprint('internalpage', __name__, url_prefix='/internalpage')

from apps.InternalPage.controller.ChannelManage import *
