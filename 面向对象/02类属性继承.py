#!/usr/bin/env python3
# coding: utf-8


class Parent(object):
    x = 1


class Child1(Parent):
    pass


class Child2(Parent):
    pass


def test():
    print(Parent.x, Child1.x, Child2.x)  # 1 1 1
    Child1.x = 2  # 注意这里用的是 类.属性
    print(Parent.x, Child1.x, Child2.x)  # 1 2 1
    Parent.x = 3  # 注意这里用的是 类.属性
    print(Parent.x, Child1.x, Child2.x)  # 3 2 3

    """
    使你困惑或是惊奇的是关于最后一行的输出是 3 2 3 而不是 3 2 1。
    为什么改变了 Parent.x 的值还会改变 Child2.x 的值，
    但是同时 Child1.x 值却没有改变？
    这个答案的关键是，在 Python 中，类变量在内部是作为字典处理的。
    如果一个变量的名字没有在当前类的字典中发现，
    将搜索祖先类（比如父类）直到被引用的变量名被找到, 
    如果这个被引用的变量名既没有在自己所在的类又没有在祖先类中找到，
    会引发一个 AttributeError 异常。
    """


if __name__ == '__main__':
    test()
