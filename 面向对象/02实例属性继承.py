#!/usr/bin/env python3
# coding: utf-8

"""父类的方法调用子类中才有的属性。

可以看到，是可以调用的。
"""


class Parent:

    def use(self):
        print(self.x)


class Child(Parent):

    def __init__(self):
        super().__init__()
        self.x = 10


def test():
    c = Child()
    c.use()


if __name__ == '__main__':
    test()
