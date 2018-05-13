#!usr/bin/env python3
# coding: utf-8

import pymssql

conn = pymssql.connect(host='192.168.1.1', user='sa', password='123')
cur = conn.cursor()

# 查看所有数据库
cur.execute('select name from sysdatabases')
list(cur.fetchall())

# 查看指定数据库中所有表
# xtype='U':表示所有用户表，xtype='S':表示所有系统表
cur.execute("select name from database..sysobjects where xtype='U' order by name")
list(cur.fetchall())

# 查看指定表中字段
cur.execute("select name from database..syscolumns id=Object_Id('table')")
list(cur.fetchall())

cur.close()
conn.close()