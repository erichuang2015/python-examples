#!/usr/bin/env python3
# coding:utf-8

r'''相关的应用是:
PIL的Image.open()是不能直接打开b"xxxx"形式的内容的,
需要先令f = BytesIO(b"xxxx")读入, 再用Image.open(f)打开
'''

from io import StringIO, BytesIO


r'''内存中写字符串'''
with StringIO() as f:
    f.write('123')
    f.write('hello')
    # 取出值
    print(f.getvalue())
# 或者
with StringIO('hello world') as f:
    print(f.getvalue())

r'''内存中写字节流(操作跟StringIO一致, 只是要传入字节流)'''
with BytesIO() as f:
    f.write('123'.encode())
    f.write('hello'.encode())
    print(f.getvalue())
# 或者
with BytesIO('hello world'.encode()) as f:
    print(f.getvalue())