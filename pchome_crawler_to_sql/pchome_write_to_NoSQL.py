import time
import requests
from pymongo import MongoClient


client = MongoClient()
client = MongoClient('127.0.0.1', 27017)

for i in range(1, 4):
    SONYSOUND_PCHOME_URL = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=sony%E9%9F%B3%E9%9F%BF&page={}&sort=sale/dc'.format(
        i)
    reqs = requests.get(SONYSOUND_PCHOME_URL)
    if reqs.status_code != requests.codes.ok:
        print(i)
        print('error', reqs.status_code)
        continue
    data = reqs.json()
    for product in data['prods']: # product本身是字典所以直接投入MongoDB
        client.pchome.products.insert_one(product)
        time.sleep(2)
