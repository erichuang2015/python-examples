#!/usr/bin/env python3
# coding: utf-8


class Test(object):
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

t = Test(3)
# t.value=3 # 错误，属性不可修改
print(t.value)


class Test2(object):
    def __init__(self, value):
        self.__value = value

    def __str__(self):
        return self.__value
        
    def __get(self):
        return self.__value

    def __set(self, value):
        self.__value = value

    def __del(self):
        del self.__value

    # 传入时要注意顺序
    value = property(__get, __set, __del)

t = Test2(3)
del t.value
