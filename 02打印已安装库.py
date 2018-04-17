#!/usr/bin/env python3
# coding:utf-8

import os
import re


def main():
    output = os.popen('pip3 list')
    pattern = re.compile(r'(.+?) \(.+?\)')
    lst = pattern.findall(output.read())
    for item in lst:
        print(item, end=' ')
    print()


if __name__ == '__main__':
    main()
