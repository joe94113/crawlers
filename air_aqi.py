import requests
import re

AIR_URL = "https://airtw.epa.gov.tw/json/camera_ddl_pic/camera_ddl_pic_2020111810.json?"

reqs = requests.get(AIR_URL)
if reqs.status_code == requests.codes.ok:
    data = reqs.json()

    # 單一搜尋
    # search_name = [d for d in data if "陽明" in d['Name']][0]['Name']

    for d in data:
        name = d['Name']
        if 'AQI' not in name:
            continue
        result = re.search(r'(.+)\(AQI=(\d+)', name)
        site_name = result.group(1)
        aqi = result.group(2)
        print(site_name, aqi)
