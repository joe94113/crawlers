import requests
from bs4 import BeautifulSoup
import pprint


# 不要SSL驗證，有HACKING方面風險
re = requests.get('https://chart.stock-ai.com/history?symbol=%5ETWII&resolution=D&from=1571401487&to=1605615947',
                  verify=False)
if re.status_code == requests.codes.ok:
    data = re.json()
    zipped = zip(data['t'], data['o'], data['h'], data['l'], data['o'], data['v'])

    # zip是iterable迭代，所以要轉為list才看的到資料
    pprint.pprint(list(zipped))
