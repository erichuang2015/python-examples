#!/usr/bin/env python3
# coding: utf-8

"""仔细比较这几种创建单例模式的方法."""


class Singleton:
    """经典单例模式1."""
    # 这里的__new__()要传入 cls, *args, **kwargs 三个参数,
    # 这是个规定.
    # *args, **kwargs 中的内容, 会传入__init__()中
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            # *注意* super().__new__()中不能传入cls以外的参数
            # 因为Singleton的父类Object的__new__只有cls一个参数
            # 注意不要把上面__new__()中的参数传进来
            # 否则出现 TypeError: object() takes no parameters 错误
            cls._instance = super().__new__(cls)
        # 这里返回时, 实例的__init__()尚未调用,
        # 所以每次调用类时, 会再执行一次__init__()
        # 可以借助这个方法, 创建不同参数的相同实例, 如:
        # A = Singleton(1)
        # B = Singleton(2)
        # 虽然它们的参数不同, 但是是同一个实例
        return cls._instance
    def __init__(self, n):
        print('Creating Singleton', n)


class Singleton2:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self, n):
        print('Creating Singleton2', n)


class SingletonMeta(type):
    def __init__(self, *args, **kwargs):
        self._instance = None # 被类继承后, 会变成类属性
        super().__init__(*args, **kwargs)
    def __call__(self, *args, **kwargs):
        if not self._instance:
            self._instance = super().__call__(*args, **kwargs)
        return self._instance
class Spam(metaclass=SingletonMeta):
    """利用元类创建单例方法1.

    继承元类的类的__new__()方法会覆盖元类的__call__()方法.

    这种方法和上面的 经典单例模式2, 本质上是*不一致*的.
    区别在__init__()执行次数上.
    """
    def __init__(self, n):
        print('Creating Spam', n)


class SingletonMeta2(type):
    _instances = {}
    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super().__call__(*args, **kwargs)
        return self._instances[self]
class Spam2(metaclass=SingletonMeta2):
    """利用元类创建单例方法2."""
    def __init__(self, n):
        print('Creating Spam2', n)


def main():
    s1 = Singleton(1) # 会打印内容
    s2 = Singleton(2) # 会打印内容
    print(s1 is s2)
    print('='*50)
    s1 = Singleton2(1) # 会打印内容
    s2 = Singleton2(2) # 会打印内容
    print(s1 is s2)
    print('='*50)
    s1 = Spam(1) # 会打印内容
    s2 = Spam(2) # 不会打印内容
    print(s1 is s2)
    print('='*50)
    s1 = Spam2(1) # 会打印内容
    s2 = Spam2(2) # 不会打印内容
    print(s1 is s2)


if __name__ == '__main__':
    main()
