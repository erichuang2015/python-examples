#!/usr/bin/env python3
# coding: utf-8

"""在控制台打印有颜色或格式的文字.

格式：\033[显示方式;前景色;背景色m你的内容\033[0m

说明:

前景色            背景色            颜色
---------------------------------------
30                40              黑色
31                41              红色
32                42              绿色
33                43              黃色
34                44              蓝色
35                45              紫红色
36                46              青蓝色
37                47              白色

显示方式           意义
-------------------------
0           终端默认设置
1             高亮显示
4            使用下划线
5              闪烁
7             反白显示
8              不可见
"""


# 前景色
COLOR = { 
    'r': 31,  # 红色
    'g': 32,  # 绿色
    'b': 34,  # 蓝色
    'y': 33,  # 黄色
    'p': 35,  # 紫红色
    'c': 36,  # 青蓝色
}


def cool(string: str, color: str=None, bold: bool=False) -> str:
    """选择控制台打印文字格式.
    
    :param string: 输出的文字内容.

    :param color: 文字前景色.
    
    :param bold: 是否高亮.
    """

    color = '%s' % COLOR.get(color, '')
    mode = '1' if bold else ''
    style = ';'.join(s for s in (mode, color) if s)
    return '\033[%sm%s\033[0m' % (style, string)


def test():
    print(cool('正常显示1'))
    print(cool('正常显示2'))
    print('*'*60)

    print('测试前景色')
    print(cool('红色', 'r'))
    print(cool('绿色', 'g'))
    print(cool('蓝色', 'b'))
    print(cool('黄色', 'y'))
    print(cool('紫红色', 'p'))
    print(cool('青蓝色', 'c'))
    print('*'*60)

    print('测试显示模式')
    print(cool('高亮', bold=True))
    print('*'*60)

    print('测试混合显示')
    print(cool('红色', 'r'))
    print(cool('红色', 'r', True))
    print('*'*60)

    print('测试非正常输入')
    print(cool('非正常输入1', '123'))
    print(cool('非正常输入2', 'hhh', True))
    print('*'*60)


if __name__ == '__main__':
    test()
