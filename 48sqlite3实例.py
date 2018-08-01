#!/usr/bin/env python3
# coding: utf-8

"""sqlite3实例.

所有修改数据库的行为都要进行提交(cursor.commit()).

数据类型
NULL	值是一个 NULL 值。
INTEGER	值是一个带符号的整数，根据值的大小存储在 1、2、3、4、6 或 8 字节中。
REAL	值是一个浮点值，存储为 8 字节的 IEEE 浮点数字。
TEXT	值是一个文本字符串，使用数据库编码（UTF-8、UTF-16BE 或 UTF-16LE）存储。
BLOB	值是一个 blob 数据，完全根据它的输入存储。

sqlite3的shell命令
.help   查看帮助
.tables 查看所有表
.schema 查看所有表字段类型
"""

import sqlite3


# 连接当前目录下的数据库, 不存在则创建
conn = sqlite3.connect('example.db')
# 创建一个游标
cursor = conn.cursor()
# 创建表, 不加"if not exists", 当表存在时会报错
# unique使该字段的值只能唯一
# check使插入的数据必须满足指定要求
# default不插入该字段, 则默认
# primary key 使字段成为主键, 每个表都必须有, 唯一标识数据库表中的各行/记录
# 注意在sqlite3中主键可以为空, 这里显示指定其不能为空
# 主键可以不指定unique, 因为其必定唯一
cursor.execute('create table if not exists "info" (\
    id integer not null,\
    name text not null unique,\
    age integer check(age > 0),\
    sex text default "male",\
    primary key(id))')
# 查看已有表
cursor.execute('select name from sqlite_master where type="table" order by name').fetchall()
# 插入指定数据
cursor.execute('insert into info values (%s, %s, %s, %s)', (0, "张三", 20, "male"))
# 插入指定数据
cursor.execute('insert into info (id, name, age) values (%s, %s, %s)', (1, "李四", 19))
# 更新数据
# where后可以跟 比较运算符, between, in, not in; 
# like(不区分大小写), '_'替代一个字符; '%'替代0个或多个字符;
# glob(区分大小写), '?'替代一个字符; '*'替代0个或多个字符;
cursor.execute('update info set name="王五" where name="张三"')
# 选择指定数据
# distinct可以消除重复;
# order by排序, desc降序, asc升序
cursor.execute('select distinct name from info where id in (0, 1) order by age desc')
# 返回选择的信息, lst是tuple构成的列表
# 如: [('王五',), ('李四',)]
lst = cursor.fetchall()
print(lst)
# 删除指定记录, 不加where, 删除所有
cursor.execute('delete from info where id=1')
# 重命名表
cursor.execute('alter table info rename to hello')
# 在表中加入新字段
cursor.execute('alter table hello add column like text')
# 删除表
cursor.execute('drop table hello')
# 关闭游标
cursor.close()
# 提交事务(不提交, 任何修改数据库的行为都不会生效)
conn.commit()
# 回滚, 撤销上一次提交
conn.rollback()
# 关闭连接
conn.close()
