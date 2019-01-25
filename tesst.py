from settings.BaseConfig import Connect_mysql


db = Connect_mysql('dm')
sql= ['select count(*) from zhuge_dm.citys_source where company_id=39 limit 1','select count(*) from zhuge_dm.city_source where company_id=39 limit 1','select count(*) from zhuge_dm.city_source where company_id=39 limit 1','select count(*) from zhuge_dm.city_source where company_id=39 limit 1']
data = db.thread_sql(sql)
print(data)
