#!/usr/bin/env python3
# coding: utf-8

"""装饰器在模块加载时执行.

通过这个例子可以很清晰的看到.
"""


registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f2()


if __name__ == '__main__':
    main()
