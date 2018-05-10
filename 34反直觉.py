#!/usr/bin/env python3
# coding: utf-8

"""一个反直觉例子."""


b = 6
def f1(a):
    #global b
    print(a)
    # 第二个print会报错
    # 原因出在`b = 9`这行上
    # 当函数中有为某变量赋值的语句, 解释器会把这个变量当成局部变量
    # 但调用print()时, b还未赋值, 所以会报错
    # 这样是有益的, 可以避免解释器偷偷修改了全局变量
    # 若要避免这个错误, 需显示指明b是全局变量(global)
    print(b)
    b = 9

f1(3)
