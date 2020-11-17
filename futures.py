import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from pprint import pprint
from threading import Thread
import json


def get_url():
    date = datetime.today()
    urls = []
    while True:
        urls.append(
            'https://www.taifex.com.tw/cht/3/futContractsDate?queryDate={}%2F{}%2F{}'.format(date.year, date.month,
                                                                                             date.day))
        date = date - timedelta(days=1)
        if date < datetime.today() - timedelta(days=5):
            break
    return urls


def crawl(url):
    print('crawling', url)
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'html.parser')
    else:
        print('connection error')

    try:
        table = soup.find('table', class_='table_f')
        trs = table.find_all('tr')
    except AttributeError:
        print('no data for', url)
        return

    rows = trs[3:]
    data = {}
    for row in rows:
        tds = row.find_all('td')
        cells = [td.text.strip() for td in tds]

        if cells[0] == '期貨小計':
            break

        if len(cells) == 15:
            product = cells[1]
            row_data = cells[1:]
        else:
            row_data = [product] + cells

        converted = [int(d.replace(',', '')) for d in row_data[2:]]
        row_data = row_data[:2] + converted

        headers = ['商品', '身份別', '交易多方口數', '交易多方金額', '交易空方口數', '交易空方金額', '交易多空淨口數', '交易多空淨額',
                   '未平倉多方口數', '未平倉多方金額', '未平倉空方口數', '未平倉空方金額', '未平倉淨口數', '未平倉多空淨額']

        # product -> who -> what
        product = row_data[0]
        who = row_data[1]
        contents = {headers[i]: row_data[i] for i in range(2, len(headers))}
        if product not in data:
            data[product] = {who: contents}
        else:
            data[product][who] = contents
    jsonStr = json.dumps(data, ensure_ascii=False)
    # print(data['小型臺指期貨']['自營商']['未平倉淨口數'])
    # pprint(data)
    return jsonStr


urls = get_url()
for url in urls:
    jsonStr = crawl(url)
pprint(jsonStr)

# threads =[]
# for i in range(5):
#     threads.append(Thread(target=crawl()))
#
# for thread in threads:
#     thread.start()
# for thread in threads:
#     thread.join()
