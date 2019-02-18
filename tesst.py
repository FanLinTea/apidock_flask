import requests
import json
Body = {'city_en': 'wuhan', 'source_en': 'youkuyijia', 'service_type': 4, 'all': '', 'type': 'string'}


city_channel_url = "http://broker.dapi.zhugefang.com/channel/detail/getChannelDmInfo"
result = requests.post(city_channel_url, data=json.dumps(Body))
print(result)