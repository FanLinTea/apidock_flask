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
    sql = f'select distinct(city_name),city from zhuge_dm.city_source where is_dock=1'
    city_dict = db.select_sql(sql)
    citys = [k['city_name'] for k in city_dict]
    city_py = [k['city'] for k in city_dict]
    # sql = f'select distinct(company_id),source_name from zhuge_dm.city_source where is_dock=1'
    # company_dict = db.select_sql(sql)
    # company_id = [k['company_id'] for k in company_dict]
    info = {'source_name': channels, 'city': citys, 'city_py': city_py}
    data = json.dumps(info)
    return data

@internalpage.route('/select_channel', methods=['POST'])
def select_channel():
    form_data = request.values
    for i in form_data:
        form_data = eval(i)

    channel = form_data.get('channel')
    city = form_data.get('city')
    info = []

    if city and not channel:
        sql = f'select distinct(source_name),service_type,user_name,city,company_id,details_key,city_name,FROM_UNIXTIME(ctime,"%Y-%m-%d")' \
              f'as ctime,id from zhuge_dm.city_source where is_dock=1 and city_name="{city}"'

        db = Connect_mysql('dm')
        data = db.select_sql(sql)
        data = json.dumps(data)
        return data

    if channel and city:
        db = Connect_mysql('dm')
        sql = f'select distinct(source_name),service_type,user_name,city,company_id,details_key,city_name,ctime' \
              f' from zhuge_dm.city_source where is_dock=1 and city_name="{city}" and source_name="{channel}"'

        data1 = db.select_sql(sql)
        city_py = data1[0]['city']

        sql = f"select source_name,FROM_UNIXTIME(A.refresh_time, '%Y-%m-%d') as time,count(*) num " \
              f"from rent_{city_py}.house_rent_gov A where company_name = '{channel}' group by time order by  time desc LIMIT 1"
        data2 = db.select_sql(sql)
        data2[0]['city_name'] = city
        info = json.dumps(data2)
        return info

    if channel and not city:
        if isinstance(channel, int):
            sql = f'select distinct(city_name),service_type,user_name,city,company_id,details_key ' \
                  f'from zhuge_dm.city_source where is_dock=1 and company_id={channel}'
        else:
            sql = f'select distinct(city_name),service_type,user_name,city,company_id,details_key ' \
                  f'from zhuge_dm.city_source where is_dock=1 and source_name="{channel}"'

        db = Connect_mysql('dm')
        data = db.select_sql(sql)

        sqls = []
        for i in data:
            city_sql = f"select source_name,FROM_UNIXTIME(A.refresh_time, '%Y-%m-%d') as time,count(*) num " \
                       f"from rent_{i['city']}.house_rent_gov A where company_id = {i['company_id']} group by time order by  time desc LIMIT 1"
            sqls.append(city_sql)
        data_all = db.thread_sql(sqls)

    citys = []
    for city_info in data_all:
        if city_info:
            city_info = city_info[0]
            source = city_info['source_name'].replace('/', '-')
            for city in data:
                if source == city['details_key']:
                    city_info['city_name'] = city['city_name']
                    channel_city = city_info
                    citys.append(city['city_name'])
                    info.append(channel_city)
                    break

    for i in data:
        if i['city_name'] not in citys:
            info.append({'city_name': i['city_name'], 'source_name': '', 'time': '空', 'num': '空'})
    info = json.dumps(info)

    return info