from apps.InternalPage.internalPage_Blueprint import internalpage
from settings.BaseConfig import Connect_mysql
from flask import request
from werkzeug.datastructures import CombinedMultiDict
import json


@internalpage.route('/all_channel', methods=['POST'])
def all_channel():
    db = Connect_mysql('dm')
    sql = f'select distinct(source_name) from zhuge_dm.city_source where is_dock=1'
    channel_dict = db.select_sql(sql)
    channels = [k['source_name'] for k in channel_dict]
    sql = f'select distinct(city_name) from zhuge_dm.city_source where is_dock=1'
    city_dict = db.select_sql(sql)
    citys = [k['city_name'] for k in city_dict]
    sql = f'select distinct(company_id) from zhuge_dm.city_source where is_dock=1'
    company_dict = db.select_sql(sql)
    company_id = [k['company_id'] for k in company_dict]
    info = {'source_name': channels, 'city': citys, 'company_id': company_id}
    data = json.dumps(info)
    return data

@internalpage.route('/select_channel', methods=['POST'])
def select_channel():
    data = request.values
    for i in data:
        data = i
    # db = Connect_mysql('dm')
    # sql = [f'select distinct(company_id),city_name,source_name from zhuge_dm.city_source where is_dock=1']
    # data = db.thread_sql(sql)
    print(data)
    return 'OK'