# import pymongo
#
# mongo = pymongo.MongoClient('mongodb://zhuge:7UgfAWbUtTKeMVGrSLwsHjB9xGjumnck@dds-2ze2f6d07e237dd41500-pub.mongodb.rds.aliyuncs.com:3717/admin')
# db = mongo.get_database('zhuge_dm')
# table = db.get_collection('api_bad_info')
# print(table)
# s = {
#     1: '小区名&室&总楼层&价格&城区&商圈 不能为空',
#     2: '一批房源中 相同url 的房源 只保留最后一条数据',
#     3: '一批房源中 同小区，同来源，同楼层，同总楼层，同室，同厅，同朝向，同面积，同价格 只保留最后一条房源',
#     4: '小区名不能为空',
#     5: '总面积异常,个人房源面积可以为空， 非个人房源， 面积<0 or 空 or 面积>50000',
#     6: '卧室个数小于0',
#     7: '总楼层小于0,空，[0，66]',
#     8: '出租价格小于等于0，大于1000000扔掉',
#     9: '预留字段目前没有用',
#     10: '下架房源',
#     11: '判重房源信息是否已存在gov表中',
#     12: '是否是同一个小区  总楼层 本楼层 面积 室 厅 价格 朝向 相同source',
#     13: 'Q房网非自身房源',
#     14: '业主房源，小区，城区，商圈 不能都为空',
#     15: '个人房源过滤经纪人房源',
#     16: '检测房源标题是否含有经纪公司关键字',
#     17: '检测房源描述是否含有经纪公司关键字',
#     18: '过滤掉整租 标题 中出现合租关键字',
#     19: '不在小区列表中',
#     20: '不在小区表中',
#     21: '检测个人房源标题关键字',
#     22: '检测个人房源描述关键字',
#     23: '业主房源去重,业主房源 同小区，同楼层，同总楼层，同室，同电话',
#     24: '去mongo查询小区信息失败的数据',
#     25: 'owner_phone房屋联系人电话是数字或者逗号，非400打头，位数不低于7不高于12',
#     26: 'source是10业主时， owner_phone是空',
#     27: 'service_phone 是数字或者逗号，400或者00400打头，位数不低于10不高于20',
#     28: 'house_toward朝向为空，暂无则设置为空，属于配置文件定义的朝向集',
#     29: 'house_fitment装修情况空，暂无则设置为空，属于文件定义的装修集',
#     31: '高，中，低 ( 整租楼层异常）',
#     32: '卫数据异常(查询gov表中总楼层最大值，10)',
#     33: '厅数据异常(查询gov表中总楼层最大值，11)',
#     34: '整租房单价<30 or 单价 >1000 的',
#     36: 'source_url不符合规则的',
#     37: '房源的图片的url验证,没有匹配到http',
#     38: '房型图片验证,没有匹配到http',
#     39: '视频看房的url地址,没有匹配到http',
#     40: 'owner_phone,service_phone 都为空',
#     41: '房源标题出现商住两用,不限购,几十年产权等关键字',
#     42: '房源描述出现商住两用,不限购,几十年产权等关键字',
#     43: 'company_id为空',
#     44: 'public_time个人保留一个月之内的，经济房源保留三个月之内的',
#     45: 'rent_type为空',
#     46: '租房个人房源owner_name出现公寓名称则过滤掉，并且下掉以前进库的房源',
#     47: '过滤掉整租 房源描述 中出现合租关键字',
#     48: '验证business_type为空',
#     49: '验证apartment_type为空',
#     50: 'business_license营业执照图片的url验证,没有匹配到http',
#     51: 'credit_card经纪人信息卡图片的url验证,没有匹配到http',
# }
# for i in s:
#     print({'bad_type': i, 'bad_info': s[i]})
#     table.insert({'bad_type': i, 'bad_info': s[i]})
#


import arrow
# t1 = arrow.now()
# t2 = arrow.utcnow()
# print(t1,t2)
date_str = arrow.utcnow()
date = date_str.utctimetuple()
print(date_str)

1548633600
1548604800