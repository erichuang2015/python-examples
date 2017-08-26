#!/usr/bin/env python3
# coding:utf-8

import sqlite3


# 连接当前目录下的数据库, 不存在则创建
db = sqlite3.connect('example.db')
# 创建一个游标
cursor = db.cursor()
# 创建表
cursor.execute('create table info ('\
    'id int primary key,'\
    'name varchar(64) not null,'\
    'age tinyint,'\
    'sex char(6))')
# 插入指定数据
cursor.execute('insert into info values(1, "张三", 20, "male")')
# 选择指定数据
cursor.execute('select id, name, age, sex from info where id = 1')
# 返回选择的信息, 类型是tuple构成的列表
lst = cursor.fetchall()
print(lst)

# 关闭游标
cursor.close()
# 提交事务(不提交, 任何修改数据库的行为都不会生效)
db.commit()
# 关闭连接
db.close()
