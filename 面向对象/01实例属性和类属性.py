#!/usr/bin/env python3

"""实例属性和类属性.

实例属性和类属性是分开的,
实例属性可以在实例的__dict__属性中找到.
类属性可以在类的__dict__属性中找到.


查找两种属性:
同名时,
实例方法优先调用实例属性, 找不到再找同名的类属性.
类方法只调用类属性.


修改两种属性:
实例方法和类方法分别操作实例属性和类属性.
当实例属性不存在时, 实例方法会创建一个实例属性,
但不推荐这样创建实例属性,
实例属性应该只在__init__()中创建.
当类属性不存在时, 类方法会创建一个类属性,
也不推荐这样创建类属性.
"""


class C:
    a = 10

    def __init__(self):
        self.a = 2222

    @classmethod
    def class_foo(cls):
        cls.a = 3333

    @classmethod
    def class_foo2(cls):
        cls.b = 4444

    def foo(self):
        self.a = 5555

    def foo2(self):
        self.c = 6666


def main():
    c = C()
    print(C.__dict__)
    print(c.__dict__)
    print(dir(C))
    print(dir(c))
    print('*' * 30)
    print('实例', c.a)
    print('类', C.a)
    c.a = 10
    print('实例', c.a)
    print('类', C.a)
    c.class_foo()
    print('实例', c.a)
    print('类', C.a)
    c.foo()
    print('实例', c.a)
    print('类', C.a)
    c.class_foo2()
    print('实例', c.b)
    print('类', C.b)
    c.foo2()
    print(c.c)


if __name__ == '__main__':
    main()
