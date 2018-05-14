#!/usr/bin/env python3
# coding: utf-8


class Singleton:
    """经典单例模式."""

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            # super()调用父类的__new__()方法
            # 所有类都默认继承自object
            # __new__中传入的cls参数不能省略
            # 但__init__中传入的self参数却不能传入
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw))
            # python3中, super()参数可以省略
            #cls.instance = super().__new__(cls, *args, **kw)
        return cls._instance


class Singleton2:
    """单例模式中的懒汉式.
    
    仅在需要时才创建.
    """

    _instance = None
    
    def __init__(self):
        if not self._instance:
            print('__init__ method called...')
        else:
            print('Instance already created:', self.get_instance())
    
    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = Singleton2()
        return cls._instance


def main():
    s1 = Singleton()
    print(s1)
    s2 = Singleton()
    print(s2)
    print('='*50)
    s1 = Singleton2()
    print('%x' % id(Singleton2))
    print('%x' % id(s1))
    print('Object created', Singleton2.get_instance())
    s2 = Singleton2()


if __name__ == '__main__':
    main()
