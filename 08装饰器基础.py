#!/usr/bin/env python3
# coding:utf-8

import functools


# 不带参数装饰器
def reg(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 带参数装饰器
def log(text):
    def decorator(func):
        # 不加这句, 会改变函数名(__name__)
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('hello world!')
    return


# 装饰器测试
if __name__ == '__main__':
    r = now()
    print(now.__name__)
