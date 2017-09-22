#!/usr/bin/env python3
# coding:utf-8

import pymongo


with pymongo.MongoClient() as ct:
    db = ct['temp']
    tb = db['temp']
    # 插入数据
    tb.insert_one({'name': 'nihao'})
    # 插入item, 若id已存在, 则放弃插入
    item = {'id':123, 'name': 'nihao'}
    tb.update_one({'id': item['id']}, {'$set': item}, True)
    # 读取数据
    lst = list(tb.find(projection={"_id":0})) # 通过projection参数过滤掉指定键, 0为不显示, 1为显示
