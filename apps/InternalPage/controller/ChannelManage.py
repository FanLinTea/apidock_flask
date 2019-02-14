from apps.InternalPage.internalPage_Blueprint import internalpage
from settings.BaseConfig import Connect_mysql,Connect_mongo
from flask import request
from werkzeug.datastructures import CombinedMultiDict
import json
import arrow


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
    '''搜索渠道或城市, 渠道and城市'''
    form_data = request.values
    for i in form_data:
        form_data = eval(i)

    channel = form_data.get('channel')
    try:
        channel = int(channel)
    except:
        pass
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
        if not data1:
            mess = {'flag': 2, 'message': '渠道没有此城市数据'}
            mess = json.dumps(mess)
            return mess
        city_py = data1[0]['city']
        user_name = data1[0]['user_name']

        db = Connect_mysql('rent')
        sql = f"select source_name,company_id,source,FROM_UNIXTIME(A.refresh_time, '%Y-%m-%d') as time,count(*) num " \
              f"from rent_{city_py}.house_rent_gov A where company_name = '{channel}' group by time order by  time desc LIMIT 1"
        data2 = db.select_sql(sql)
        data2[0]['city_name'] = city
        data2[0]['city_py'] = city_py
        data2[0]['user_name'] = user_name
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
            city_sql = f"select source_name,company_id,source,FROM_UNIXTIME(A.refresh_time, '%Y-%m-%d') as time,count(*) num " \
                       f"from rent_{i['city']}.house_rent_gov A where company_id = {i['company_id']} group by time order by time desc LIMIT 1"
            sqls.append(city_sql)
        db = Connect_mysql('rent')
        data_all = db.thread_sql(sqls)

    citys = []
    for city_info in data_all:
        if city_info:
            city_info = city_info[0]
            source = city_info['source_name'].replace('/', '-')
            for city in data:
                if source == city['details_key']:
                    city_info['city_py'] = city['city']
                    city_info['city_name'] = city['city_name']
                    city_info['user_name'] = city['user_name']
                    citys.append(city['city_name'])
                    info.append(city_info)
                    break

    for i in data:
        if i['city_name'] not in citys:
            info.append({'city_name': i['city_name'], 'source_name': '', 'time': '空', 'num': '空', 'source': '','company_id':''})
    info = json.dumps(info)

    return info

@internalpage.route('/bad_info', methods=['POST'])
def bad_info():
    '''查询bad量和信息'''
    request_info = request.values
    for i in request_info:
        request_info = eval(i)
    company_id = request_info.get('company_id')
    city = request_info.get('city_py')
    source = request_info.get('source')

    sql = f"select count(1) as count,FROM_UNIXTIME(bad.refresh_time, '%Y-%m-%d') as time from rent_{city}.house_rent_gov as bad where company_id={company_id} and source={source} and refresh_time > unix_timestamp((select FROM_UNIXTIME(tab.refresh_time, '%Y-%m-%d') as time from rent_{city}.house_rent_gov as tab where company_id={company_id} and source={source} order by refresh_time desc limit 1))"
    db = Connect_mysql('rent')
    gov_count = db.select_sql(sql)

    db = Connect_mysql('bad_mysql')
    # sql = f"select bad_type,count(1) as num,FROM_UNIXTIME(bad.updated, '%Y-%m-%d') as time from rent_{city}.house_rent_bad as bad where company_id={company_id} and source={source} and updated > unix_timestamp((select FROM_UNIXTIME(tab.updated, '%Y-%m-%d') as time from rent_{city}.house_rent_bad as tab where company_id={company_id} and source={source} order by updated desc limit 1)) group by bad_type"
    date_str = arrow.get(gov_count[0]['time'], "YYYY-MM-DD")
    date_end = arrow.get(gov_count[0]['time'], "YYYY-MM-DD").shift(days=1)
    date_str = date_str.timestamp - 28800
    date_end = date_end.timestamp - 28800
    sql = f"select bad_type,count(1) as num,FROM_UNIXTIME(bad.updated, '%Y-%m-%d') as time from rent_{city}.house_rent_bad as bad " \
          f"where updated BETWEEN {date_str} and {date_end} and company_id={company_id} and source={source} group by bad_type"
    data = db.select_sql(sql)
    info = {}
    info['gov'] = gov_count[0]

    mongo = Connect_mongo('dios').Conn('zhuge_dm', 'api_bad_info')
    for bad in data:
        bad_info = mongo.find_one({'bad_type': bad['bad_type']})
        bad['bad_info'] = bad_info['bad_info']

    info['bad'] = data
    info = json.dumps(info)
    return info

@internalpage.route('/select_time', methods=['POST'])
def select_time():
    request_info = request.values
    for i in request_info:
        request_info = eval(i)
    start_time = request_info.get('time')[0]
    start_time = arrow.get(start_time, "YYYY-MM-DD")
    start_time = start_time.timestamp - 28800
    ent_time = request_info.get('time')[1]
    ent_time = arrow.get(ent_time, "YYYY-MM-DD")
    ent_time = ent_time.timestamp - 28800
    city = request_info.get('data').get('city_py')
    source = request_info.get('data').get('source')
    company_id = request_info.get('data').get('company_id')

    db = Connect_mysql('rent')
    sql = f'select count(*) as count from rent_{city}.house_rent_gov where company_id={company_id} and source={source} and refresh_time between {start_time} and {ent_time}'
    gov_num = db.select_sql(sql)
    print(gov_num)
    info = {}
    info['gov'] = gov_num[0]

    db = Connect_mysql('bad_mysql')
    sql = f"select bad_type,count(1) as num from rent_{city}.house_rent_bad as bad " \
          f"where updated BETWEEN {start_time} and {ent_time} and company_id={company_id} and source={source} group by bad_type"
    data = db.select_sql(sql)

    mongo = Connect_mongo('dios').Conn('zhuge_dm', 'api_bad_info')
    for bad in data:
        bad_info = mongo.find_one({'bad_type': bad['bad_type']})
        bad['bad_info'] = bad_info['bad_info']

    info['bad'] = data
    info = json.dumps(info)
    return info
    # timeoo = "2019-02-13"
    # t = arrow.get(timeoo, "YYYY-MM-DD")
    # print(t.timestamp - 28800)