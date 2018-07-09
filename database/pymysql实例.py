#!/usr/bin/env python3
# coding: utf-8

"""pymssql实例.

和sqlite3用法基本一致.
"""

import pymysql


# 不指定主机和端口, 默认本机
# 需要指定utf8编码, 不然显示不出中文
db = pymysql.connect(user='root', passwd='123', db='people', charset='utf8')
# 创建一个游标
cursor = db.cursor()
# 执行一条语句
cursor.execute("select * from info")
# 返回选择的信息, 类型是tuple构成的列表
lst = cursor.fetchall()
print(lst)

# 关闭游标
cursor.close()
# 提交事务(不提交, 任何修改数据库的行为都不会生效)
db.commit()
# 关闭连接
db.close()