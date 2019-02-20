from apps.InternalPage.internalPage_Blueprint import internalpage
from settings.BaseConfig import Connect_mysql, Connect_mongo
from flask import request
from werkzeug.datastructures import CombinedMultiDict
from settings.db_config import old_city
import json
import arrow
import time


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
    # 如果用户传入的是 company_id 需要把字符串转换为Int
    try:
        channel = int(channel)
    except:
        pass
    city = form_data.get('city')
    info = []

    db = Connect_mysql('dm')
    if city and not channel:
        sql = f'select distinct(source_name),service_type,source_id as source,user_name,city as city_py,company_id,details_key,city_name,FROM_UNIXTIME(ctime,"%Y-%m-%d") as ctime,id from zhuge_dm.city_source where is_dock=1 and city_name="{city}"'
        db = Connect_mysql('dm')
        data = db.select_sql(sql)
        data = json.dumps(data)
        return data

    rent_db = Connect_mysql('rent')
    sell_db = Connect_mysql('sell_mysql')
    new_sell_db = Connect_mysql('new_sell_mysql')
    if channel and city:
        if isinstance(channel, int):
            sql = f'select distinct(source_name),service_type,user_name,city,company_id,source_id,details_key,city_name,ctime' \
                  f' from zhuge_dm.city_source where is_dock=1 and city_name="{city}" and company_id="{channel}"'
        else:
            sql = f'select distinct(source_name),service_type,user_name,city,company_id,source_id,details_key,city_name,ctime' \
                  f' from zhuge_dm.city_source where is_dock=1 and city_name="{city}" and source_name="{channel}"'
        data1 = db.select_sql(sql)
        if not data1:
            mess = {'flag': 2, 'message': '渠道没有此城市数据'}
            mess = json.dumps(mess)
            return mess

        all_type_data = []
        for i in data1:
            # 提取善德表的字段 作为执行Gov表查询的条件
            city_py = i['city']
            city_name = i['city_name']
            user_name = i['user_name']
            service_type = i['service_type']
            company_id = i['company_id']
            source_id = i['source_id']
            source_name = i['details_key']
            # 由于二手房和租房分实例和库,所以根据service_type去不同库查询
            if service_type == 1:
                if city_py == 'bj':
                    sql = f"select source_name,company_id,source,FROM_UNIXTIME(max(A.refresh_time), '%Y-%m-%d') as time,count(*) num " \
                          f"from spider.house_sell_gov A where company_id = {company_id} and source = {source_id} " \
                          f"and status=1 and source_type=5"
                else:
                    sql = f"select source_name,company_id,source,FROM_UNIXTIME(max(A.refresh_time), '%Y-%m-%d') as time,count(*) num " \
                          f"from spider_{city_py}.house_sell_gov A where company_id = {company_id} and source = {source_id}     " \
                          f"and status=1 and source_type=5"
                #  新旧实例切库查询
                if city_py in old_city:
                    channel_data = sell_db.select_sql(sql)[0]
                else:
                    channel_data = new_sell_db.select_sql(sql)[0]
                channel_data['service_type'] = service_type
                channel_data['user_name'] = user_name
                channel_data['city_py'] = city_py
                channel_data['city_name'] = city_name
                if not channel_data.get('source_name'):
                    channel_data['source_name'] = source_name
                # 同一渠道可能同时包含 二手房 和租房 把他们放入列表
                all_type_data.append(channel_data)

            else:
                sql = f"select source_name,company_id,source,FROM_UNIXTIME(max(A.refresh_time), '%Y-%m-%d') as time,count(*) num " \
                      f"from rent_{city_py}.house_rent_gov A where company_id = {company_id} and source = {source_id} " \
                      f"and status=1 and source_type=5"
                channel_data = rent_db.select_sql(sql)[0]
                channel_data['service_type'] = service_type
                channel_data['user_name'] = user_name
                channel_data['city_py'] = city_py
                channel_data['city_name'] = city_name
                if not channel_data.get('source_name'):
                    channel_data['source_name'] = source_name
                all_type_data.append(channel_data)
        info = json.dumps(all_type_data)
        return info

    if channel and not city:
        if isinstance(channel, int):
            sql = f'select distinct(city_name),service_type,user_name,city,company_id,details_key,source_id,city_en ' \
                  f'from zhuge_dm.city_source where is_dock=1 and company_id={channel}'
        else:
            sql = f'select distinct(city_name),service_type,user_name,city,company_id,details_key,source_id,city_en ' \
                  f'from zhuge_dm.city_source where is_dock=1 and source_name="{channel}"'
        data = db.select_sql(sql)
        all_type_data = []
        old_city_sqls = []
        new_city_sqls = []
        rent_city_sqls = []
        for i in data:
            city_py = i['city']
            city_name = i['city_name']
            user_name = i['user_name']
            service_type = i['service_type']
            company_id = i['company_id']
            source_id = i['source_id']
            source_name = i['details_key']
            if service_type == 1:
                if city_py == 'bj':
                    sql = f"select source_name,company_id,source,FROM_UNIXTIME(max(A.refresh_time), '%Y-%m-%d') as time,count(*) num " \
                          f"from spider.house_sell_gov A where company_id = {company_id} and source = {source_id} and status=1 " \
                          f"and source_type=5"
                else:
                    sql = f"select source_name,company_id,source,FROM_UNIXTIME(max(A.refresh_time), '%Y-%m-%d') as time,count(*) num " \
                          f"from spider_{city_py}.house_sell_gov A where company_id = {company_id} and source = {source_id} and status=1 " \
                          f"and source_type=5"
                if city_py in old_city:
                    old_city_sqls.append(sql)
                else:
                    new_city_sqls.append(sql)

            else:
                sql = f"select source_name,company_id,source,FROM_UNIXTIME(max(A.refresh_time), '%Y-%m-%d') as time,count(*) num " \
                      f"from rent_{city_py}.house_rent_gov A where company_id = {company_id} and source = {source_id} and status=1 " \
                      f"and source_type=5"
                rent_city_sqls.append(sql)

        if old_city_sqls:
            old_city_data = sell_db.thread_sql(old_city_sqls)
            for i in old_city_data:
                i = i[0]
                if not i.get('source_name'):
                    continue
                else:
                    city_old = i.get('source_name')
                for u in data:
                    if u['city_en'] in city_old:
                        i['city_py'] = u['city']
                        i['service_type'] = u['service_type']
                        i['city_name'] = u['city_name']
                        i['user_name'] = u['user_name']
                        all_type_data.append(i)
                        break

        if new_city_sqls:
            new_city_data = new_sell_db.thread_sql(new_city_sqls)
            for i in new_city_data:
                i = i[0]
                if not i.get('source_name'):
                    continue
                else:
                    city_old = i.get('source_name')
                for u in data:
                    if u['city_en'] in city_old:
                        i['city_py'] = u['city']
                        i['service_type'] = u['service_type']
                        i['city_name'] = u['city_name']
                        i['user_name'] = u['user_name']
                        all_type_data.append(i)
                        break

        if rent_city_sqls:
            rent_city_data = rent_db.thread_sql(rent_city_sqls)
            for i in rent_city_data:
                i = i[0]
                if not i.get('source_name'):
                    continue
                else:
                    city_old = i.get('source_name')
                for u in data:
                    if u['city_en'] in city_old:
                        i['city_py'] = u['city']
                        i['service_type'] = u['service_type']
                        i['city_name'] = u['city_name']
                        i['user_name'] = u['user_name']
                        all_type_data.append(i)
                        break

        all_type_data = json.dumps(all_type_data)
        return all_type_data


@internalpage.route('/bad_info', methods=['POST'])
def bad_info():
    '''查询gov,bad量和信息'''
    request_info = request.values
    for i in request_info:
        request_info = eval(i)
    print(request_info)
    company_id = request_info.get('company_id')
    city = request_info.get('city_py')
    source = request_info.get('source')
    service_type = request_info.get('service_type')

    db = Connect_mysql('sell_mysql')
    new_db = Connect_mysql('new_sell_mysql')
    if service_type == 1:
        if city == 'bj':
            sql = f"select count(1) as count,FROM_UNIXTIME(bad.refresh_time, '%Y-%m-%d') as time " \
                  f"from spider.house_sell_gov as bad where company_id={company_id} and source={source} " \
                  f"and source_type=5 and status=1 " \
                  f"and refresh_time > unix_timestamp((select FROM_UNIXTIME(tab.refresh_time, '%Y-%m-%d') as time " \
                  f"from spider.house_sell_gov as tab where company_id={company_id} and source={source} order by refresh_time desc limit 1))"
        else:
            sql = f"select count(1) as count,FROM_UNIXTIME(bad.refresh_time, '%Y-%m-%d') as time " \
                  f"from spider_{city}.house_sell_gov as bad where company_id={company_id} and source={source} " \
                  f"and source_type=5 and status=1 " \
                  f"and refresh_time > unix_timestamp((select FROM_UNIXTIME(tab.refresh_time, '%Y-%m-%d') as time " \
                  f"from spider_{city}.house_sell_gov as tab where company_id={company_id} and source={source} " \
                  f"order by refresh_time desc limit 1))"
        if city in old_city:
            gov_count = db.select_sql(sql)
        else:
            gov_count = new_db.select_sql(sql)
    else:
        sql = f"select count(1) as count,FROM_UNIXTIME(bad.refresh_time, '%Y-%m-%d') as time " \
              f"from rent_{city}.house_rent_gov as bad where company_id={company_id} and source={source} " \
              f"and source_type=5 and status=1 " \
              f"and refresh_time > unix_timestamp((select FROM_UNIXTIME(tab.refresh_time, '%Y-%m-%d') as time " \
              f"from rent_{city}.house_rent_gov as tab where company_id={company_id} and source={source} order by refresh_time desc limit 1))"
        db = Connect_mysql('rent')
        gov_count = db.select_sql(sql)

    date_str = arrow.get(gov_count[0]['time'], "YYYY-MM-DD")
    date_end = arrow.get(gov_count[0]['time'], "YYYY-MM-DD").shift(days=1)
    date_str = date_str.timestamp - 28800
    date_end = date_end.timestamp - 28800
    if service_type == 1:
        sql = f"select bad_type,count(1) as num,FROM_UNIXTIME(bad.updated, '%Y-%m-%d') as time from spider_{city}.house_sell_bad as bad " \
              f"where updated BETWEEN {date_str} and {date_end} and company_id={company_id} and source={source} group by bad_type"
    else:
        sql = f"select bad_type,count(1) as num,FROM_UNIXTIME(bad.updated, '%Y-%m-%d') as time from rent_{city}.house_rent_bad as bad " \
              f"where updated BETWEEN {date_str} and {date_end} and company_id={company_id} and source={source} group by bad_type"
    db = Connect_mysql('bad_mysql')
    data = db.select_sql(sql)
    info = {}
    info['gov'] = gov_count[0]

    if service_type == 1:
        mongo = Connect_mongo('dios').Conn('zhuge_dm', 'sell_bad_info')
    else:
        mongo = Connect_mongo('dios').Conn('zhuge_dm', 'rent_bad_info')
    for bad in data:
        bad_info = mongo.find_one({'bad_type': bad['bad_type']})
        if bad_info:
            bad['bad_info'] = bad_info['bad_info']
        else:
            bad['bad_info'] = f'Mongo缺少bad类型 {bad["bad_type"]}'

    info['bad'] = data
    info = json.dumps(info)
    return info


@internalpage.route('/select_time', methods=['POST'])
def select_time():
    request_info = request.values
    for i in request_info:
        request_info = eval(i)
    print(request_info)
    start_time = request_info.get('time')[0]
    start_time = arrow.get(start_time, "YYYY-MM-DD")
    start_time = start_time.timestamp - 28800
    ent_time = request_info.get('time')[1]
    ent_time = arrow.get(ent_time, "YYYY-MM-DD")
    ent_time = ent_time.timestamp - 28800

    if start_time == ent_time:
        ent_time += 86400
    city = request_info.get('data').get('city_py')
    source = request_info.get('data').get('source')
    company_id = request_info.get('data').get('company_id')
    service_type = request_info.get('data').get('service_type')

    db = Connect_mysql('sell_mysql')
    new_db = Connect_mysql('new_sell_mysql')
    if service_type == 1:
        if city == 'bj':
            sql = f"select count(1) as count,FROM_UNIXTIME(bad.refresh_time, '%Y-%m-%d') as time " \
                  f"from spider.house_sell_gov as bad where company_id={company_id} and source={source} " \
                  f"and source_type=5 and status=1 " \
                  f"and refresh_time between {start_time} and {ent_time}"
        else:
            sql = f"select count(1) as count,FROM_UNIXTIME(bad.refresh_time, '%Y-%m-%d') as time " \
                  f"from spider_{city}.house_sell_gov as bad where company_id={company_id} and source={source} " \
                  f"and source_type=5 and status=1 " \
                  f"and refresh_time between {start_time} and {ent_time}"
        print('二手房:', sql)
        if city in old_city:
            gov_count = db.select_sql(sql)
        else:
            gov_count = new_db.select_sql(sql)
    else:
        sql = f"select count(1) as count,FROM_UNIXTIME(bad.refresh_time, '%Y-%m-%d') as time " \
              f"from rent_{city}.house_rent_gov as bad where company_id={company_id} and source={source} " \
              f"and source_type=5 and status=1 " \
              f"and refresh_time between {start_time} and {ent_time}"
        print('NEW二手房', sql)
        db = Connect_mysql('rent')
        gov_count = db.select_sql(sql)

    if service_type == 1:
        sql = f"select bad_type,count(1) as num,FROM_UNIXTIME(bad.updated, '%Y-%m-%d') as time from spider_{city}.house_sell_bad as bad " \
              f"where updated BETWEEN {start_time} and {ent_time} and company_id={company_id} and source={source} group by bad_type"
    else:
        sql = f"select bad_type,count(1) as num,FROM_UNIXTIME(bad.updated, '%Y-%m-%d') as time from rent_{city}.house_rent_bad as bad " \
              f"where updated BETWEEN {start_time} and {ent_time} and company_id={company_id} and source={source} group by bad_type"
    print(sql)
    db = Connect_mysql('bad_mysql')
    data = db.select_sql(sql)
    info = {}
    info['gov'] = gov_count[0]

    if service_type == 1:
        mongo = Connect_mongo('dios').Conn('zhuge_dm', 'sell_bad_info')
    else:
        mongo = Connect_mongo('dios').Conn('zhuge_dm', 'rent_bad_info')
    for bad in data:
        bad_info = mongo.find_one({'bad_type': bad['bad_type']})
        if bad_info:
            bad['bad_info'] = bad_info['bad_info']
        else:
            bad['bad_info'] = f'Mongo缺少bad类型 {bad["bad_type"]}'

    info['bad'] = data
    info = json.dumps(info)
    return info


@internalpage.route('/data_tab', methods=['POST'])
def data_tab():
    request_info = request.values
    for i in request_info:
        request_info = eval(i)
    start_time = request_info.get('start_time')
    start_time = arrow.get(start_time, "YYYY-MM-DD")
    start_time = start_time.timestamp - 28800
    ent_time = request_info.get('ent_time')
    ent_time = arrow.get(ent_time, "YYYY-MM-DD")
    ent_time = ent_time.timestamp - 28800
    if start_time == ent_time:
        ent_time += 86400
    source = request_info.get('source')
    company_id = request_info.get('company_id')
    bad_type = request_info.get('bad_type')
    city = request_info.get('city_py')
    service_type = request_info.get('service_type')

    db = Connect_mysql('bad_mysql')
    if service_type == 1:
        sql = f'select * from spider_{city}.house_sell_bad WHERE company_id={company_id} and source={source} and bad_type={bad_type} and updated BETWEEN {start_time} and {ent_time} LIMIT 5'
    else:
        sql = f'select * from rent_{city}.house_rent_bad WHERE company_id={company_id} and source={source} and bad_type={bad_type} and updated BETWEEN {start_time} and {ent_time} LIMIT 5'
    data = db.select_sql(sql)
    data = json.dumps(data)
    return data
