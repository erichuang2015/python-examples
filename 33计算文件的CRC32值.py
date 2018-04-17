#!/usr/bin/env python3
# coding:utf-8

import os
import sys
import zlib


filename = sys.argv[1]
# 判断是否是文件
if os.path.isfile(filename):
    with open(filename, 'rb') as f:
        contents = f.read()
    print(zlib.crc32(contents))
else:
    print('file not exists')
