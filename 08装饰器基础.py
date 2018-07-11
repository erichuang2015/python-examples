#!/usr/bin/env python3
# coding: utf-8

import functools


# 不带参数装饰器
def reg(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)
    return wrapper


# 带参数装饰器
def log(text):
    print('log') # 会被打印, 即使没有调用被装饰的函数

    def inner(func):
        print('inner') # 会被打印, 即使没有调用被装饰的函数
        # 不加这句, 会改变函数名(__name__)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return inner


@log('execute')  # 装饰器最内层以外内容在模块加载时执行!
def now():
    print('hello world!')
    return


# 装饰器测试
if __name__ == '__main__':
    pass
