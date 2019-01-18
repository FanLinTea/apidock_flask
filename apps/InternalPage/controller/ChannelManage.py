from apps.InternalPage.internalPage_Blueprint import internalpage
from settings.BaseConfig import Connect_mysql
from flask import request
import json

@internalpage.route('/select_channel', methods=['POST'])
def all_channel():
    print(request.form)
    data = request.form['name']
    # print(json.loads(data))
    print(data)
    db = Connect_mysql('dm')
    sql = [f'select distinct(company_id),city_name,source_name from zhuge_dm.city_source where is_dock=1']
    data = db.thread_sql(sql)
    return 'OK'