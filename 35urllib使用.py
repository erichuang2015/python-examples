#!/usr/bin/env python3
# coding: utf-8

from urllib import request


def main():
    with request.urlopen('http://m.ip138.com') as response:
        print(response.read().decode('utf-8'))
        # 打印状态
        print(response.status)
        # 打印头部
        print(response.getheaders())


if __name__ == '__main__':
    main()
