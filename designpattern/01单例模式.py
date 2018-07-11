#!/usr/bin/env python3
# coding: utf-8

"""仔细比较这几种创建单例模式的方法, 它们是有区别的."""


class Singleton:
    """经典单例模式1.
    
    __init__()会多次执行, 虽然是同一个实例, 如:
    A = Singleton(1)
    B = Singleton(2)
    虽然它们的参数不同, 但是是同一个实例.
    可以借助这个方法, 修改实例的属性.
    """
    # 这里的__new__()要传入 cls, *args, **kwargs 三个参数
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
        return cls._instance
    def __init__(self, n):
        self.n = n
        print('Creating Singleton', self.n)


class Singleton2:
    """经典单例模式2.
    
    __init__()会多次执行.
    """
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self, n):
        self.n = n
        print('Creating Singleton2', self.n)


class SingletonMeta(type):
    def __init__(self, *args, **kwargs):
        self._instance = None # 会变成元类创建的类的类属性
        super().__init__(*args, **kwargs)
    def __call__(self, *args, **kwargs):
        if not self._instance:
            # __call__()会调用__init__(), 
            # 所以以后再创建实例时, __init__()不会再执行
            self._instance = super().__call__(*args, **kwargs)
        # 这里返回的实例和Singleton2中__new__()返回的是不同的
        # 这里返回的是调用了__init__()的实例,
        # Singleton2的__new__()中返回的是没调用__init__()的实例
        return self._instance
class Spam(metaclass=SingletonMeta):
    """利用元类创建单例方法1.

    注意与Singleton2对比, __init__()不会多次执行,
    原因出在元类的__call__()返回的是执行了__init__()的实例,
    而Singleton2的__new__()返回的是未执行__init__()的实例,
    还会自动执行一次__init__().
    """
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self, n):
        self.n = n
        print('Creating Spam', self.n)


class SingletonMeta2(type):
    _instances = {} # 元类的元类属性, 所有它创建的类共享; 对比类的类属性
    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super().__call__(*args, **kwargs)
        return self._instances[self]
class Spam2(metaclass=SingletonMeta2):
    """利用元类创建单例方法2.

    __init__()不会多次执行.
    """
    def __init__(self, n):
        self.n = n
        print('Creating Spam2', self.n)


def main():
    print('='*50)
    s1 = Singleton(1) # 会打印内容
    s2 = Singleton(2) # 会打印内容
    print(s1 is s2)
    print(s1.n) # s1属性被修改
    print('='*50)
    s1 = Singleton2(1) # 会打印内容
    s2 = Singleton2(2) # 会打印内容
    print(s1 is s2)
    print(s1.n) # s1属性被修改
    print('='*50)
    s1 = Spam(1) # 会打印内容
    s2 = Spam(2) # 不会打印内容
    print(s1 is s2)
    print(s1.n) # s1属性未被修改
    print('='*50)
    s1 = Spam2(1) # 会打印内容
    s2 = Spam2(2) # 不会打印内容
    print(s1 is s2)
    print(s1.n) # s1属性未被修改
    print('='*50)


if __name__ == '__main__':
    main()
