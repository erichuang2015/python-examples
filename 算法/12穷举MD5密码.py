#!/usr/bin/env python3
# coding: utf-8

"""穷举法破解MD5密码, 假设元素不重复."""

from hashlib import md5
from string import ascii_letters, digits
from itertools import permutations  # 排列数

from scipy import special as S


# 假设密码是字母和数字的组合
all_letters = ascii_letters + digits


def decrypt_md5(md5_value):
    if len(md5_value) != 32:
        print('错误!')
        return

    md5_value = md5_value.lower()

    # 消耗的时间会很恐怖
    for k in range(5, 10):
        n = int(S.perm(len(all_letters), k))
        print('本轮需尝试次数:', n)
        for i, item in enumerate(permutations(all_letters, k), 1):
            code = ''.join(item)
            if md5(code.encode()).hexdigest() == md5_value:
                return code, i + (k - 5) * n


def main():
    md5_value = md5('abcdz'.encode()).hexdigest()
    result = decrypt_md5(md5_value)
    if result:
        print('\n成功 ==> {}, 尝试次数 ==> {}'.format(result[0], result[1]))
    else:
        print('\n失败!')


if __name__ == '__main__':
    main()
