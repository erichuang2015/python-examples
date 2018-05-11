#!/usr/bin/env python3
# coding: utf-8

"""流畅的python中的例子.

对于使用的编码, 总是应该显示的指定, 如调用`open()`时
"""

import sys
import locale


def main():
    # 编码优先采用`locale.getpreferredencoding()`指定的
    expressions = """
        locale.getpreferredencoding()
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
    """

    with open('00test.py', 'r') as my_file:
        for expression in expressions.split():
            value = eval(expression)
            print(expression.rjust(30), '->', repr(value))


if __name__ == '__main__':
    main()
