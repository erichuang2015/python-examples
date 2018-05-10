#!/usr/bin/env python3
# coding: utf-8


class Singleton:

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            # super()调用父类的__new__()方法
            # 所有类都默认继承自object
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
            # python3中, super()参数可以省略
            #cls.instance = super().__new__(cls, *args, **kw)
        return cls._instance


def main():
    s1 = Singleton()
    print(s1)
    s2 = Singleton()
    print(s2)


if __name__ == '__main__':
    main()
