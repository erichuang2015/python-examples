#!/usr/bin/env python3
# coding: utf-8

import logging
logging.basicConfig(level=logging.INFO)


def main():
    s = '0'
    n = int(s)
    logging.info('n = %d' % n)
    print(10 / n)


if __name__ == '__main__':
    main()
