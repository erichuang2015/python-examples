#!/usr/bin/env python3
# coding: utf-8

import os
import zlib


def main():
    filename = '00test.py'
    # 判断是否是文件
    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            contents = f.read()
        print(zlib.crc32(contents))
    else:
        print('file not exists')


if __name__ == '__main__':
    main()
