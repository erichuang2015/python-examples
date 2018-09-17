#!/usr/bin/env python3
# coding: utf-8

"""列出常规对象没有, 而函数特有的属性."""


class C:
    pass


def func():
    pass


def main():
    # 函数独有属性列表
    name_lst = sorted(set(dir(func)) - set(dir(C)))
    
    # 属性注解
    comment_lst = """
        参数和返回值的注解
        实现()运算符; 即可调用对象协议
        函数闭包, 即自由变量的绑定, 通常是None
        编译成字节码的函数元数据和函数定义体
        位置参数和关键字参数的默认值
        实现只读描述符协议
        函数所在模块中的全局变量
        命名关键字参数的默认值
        函数名称
        函数的限定名称, 如 `Random.choice`
    """

    print('{0:<30}{1:<30}'.format('名称', '说明'))
    for name, comment in zip(name_lst, comment_lst.split('\n')[1:]):
        print('{0:<30}{1:<30}'.format(name, comment))


if __name__ == '__main__':
    main()
