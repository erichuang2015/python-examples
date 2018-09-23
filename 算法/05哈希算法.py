#!/usr/bin/env python3
# coding: utf-8

"""
"""

import hashlib


def main():
    print('可用算法：{}'.format(
        ', '.join(sorted(hashlib.algorithms_available))))
    print('*' * 50)

    lorem = '''Lorem ipsum dolor sit amet, consectetur adipisicing
    elit, sed do eiusmod tempor incididunt ut labore et dolore magna
    aliqua. Ut enim ad minim veniam, quis nostrud exercitation
    ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis
    aute irure dolor in reprehenderit in voluptate velit esse cillum
    dolore eu fugiat nulla pariatur. Excepteur sint occaecat
    cupidatat non proident, sunt in culpa qui officia deserunt
    mollit anim id est laborum.'''

    # MD5
    h = hashlib.md5()
    h.update(lorem.encode('utf-8'))
    print(h.hexdigest())
    print('*' * 50)

    # SHA1
    h = hashlib.sha1()
    h.update(lorem.encode('utf-8'))
    print(h.hexdigest())
    print('*' * 50)

    # 根据名字调用指定算法
    hash_name = 'SHA512'
    h = hashlib.new(hash_name)
    h.update(lorem.encode('utf-8'))
    print(h.hexdigest())
    print('*' * 50)


if __name__ == '__main__':
    main()
