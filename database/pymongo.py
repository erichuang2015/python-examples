#!/usr/bin/env python3
# coding: utf-8

"""pymongo实例."""

import pymongo


conn = pymongo.MongoClient()
db = conn['temp']
tb = db['temp']

item = {'id':123, 'name': 'nihao'}
# 插入数据
tb.insert_one(item)
# 插入item, 若id已存在, 则放弃插入
tb.update_one({'id': item['id']}, {'$set': item}, True)

# 读取数据
# 通过projection参数过滤掉指定键, 0为不显示, 1为显示
lst = list(tb.find(projection={"_id":0}))

conn.close()
