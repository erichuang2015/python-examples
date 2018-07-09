#!/usr/bin/env python3
# coding: utf-8

"""使用property限制实例修改属性, 或者控制传入的值符合属性要求."""


class Test(object):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

t = Test(3)
#t.value = 3 # 错误，属性不可修改


class Test2(object):
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return self._value
        
    def _get(self):
        return self._value

    def _set(self, value):
        self._value = value

    def _del(self):
        del self._value

    # 传入时要注意顺序
    # 与property的参数一一对应
    value = property(_get, _set, _del)

t = Test2(3)
t.value = 4
del t.value


class Test3(object):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @value.deleter
    def value(self):
        del self._value

t = Test3(3)
t.value = 4
del t.value