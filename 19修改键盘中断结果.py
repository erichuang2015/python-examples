#!/usr/bin/env python3
# coding:utf-8

import time


def main():
    start = time.time()
    try:
        for i in range(6):
            print('hello world!')
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        end = time.time()
        finished = end - start
        print('\n[Finished in %.3fs]\n' % finished)


if __name__ == '__main__':
    main()
