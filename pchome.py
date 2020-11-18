import requests


SONYSOUND_PCHOME_URL = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=sony%E9%9F%B3%E9%9F%BF&page=1&sort=sale/dc'
reqs = requests.get(SONYSOUND_PCHOME_URL)
if reqs.status_code == requests.codes.ok:
    data = reqs.json()
    for product in data['prods']:
        print(product['name'])
        print(product[0]['price'])