#!/usr/bin/env python3
# coding: utf-8

"""Python 中压缩，解压缩。
"""

import gzip
import bz2


def main():

    """解压缩"""
    with gzip.open('somefile.gz', 'r') as f:
        text1 = f.read()
    with bz2.open('somefile.bz2', 'r') as f:
        text2 = f.read()

    """压缩"""
    with gzip.open('somefile.gz', 'w') as f:
        f.write(text1)
    with bz2.open('somefile.bz2', 'w') as f:
        f.write(text2)


if __name__ == '__main__':
    main()

