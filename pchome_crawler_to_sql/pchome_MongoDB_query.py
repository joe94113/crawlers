from pymongo import MongoClient


client = MongoClient()
db = client.pchome
coll = db.products

# 找全部
# data = coll.find()
#
# 找單一用regex，不包括大小寫
# data = coll.find({'name': {'$regex': '.*sony.*', '$options': 'i'}})
#
# 找價錢大於6000 Comparson Query Operators
# data = coll.find({'price': {'$gt': 6000}})
#
# and 串接
# name_condition = {'name': {'$regex': '.*sony.*', '$options': 'i'}}
# price_condition = {'price': {'$gt': 6000}}
# data = coll.find({'$and': [name_condition, price_condition]})
# for d in data:
#     print(d['name'], d['price'])
#
# 更新一個項目
# coll.update_one({'name': 'SONY 7.2聲道AV擴大機 STR-DH790'}, {'$set': {'price': 6000}})
#
# 如果沒有這筆資料就加入 upsert example
# coll.update_one({'name': 'sony good'}, {'$set': {'price': 100000}}, upsert=True)
#
# 刪除一個項目
# coll.delete_one({'name': 'sony good'})

