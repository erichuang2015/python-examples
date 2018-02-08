#!/usr/bin/env python3
# coding:utf-8

r'''在控制台打印有颜色或格式的文字

格式：\033[显示方式;前景色;背景色m

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

例子：
\033[1;31;40m    <!--1-高亮显示 31-前景色红色  40-背景色黑色-->
\033[0m          <!--采用终端默认设置，即取消颜色设置-->]]]
'''


STYLE = {
        'fore':
        {   # 前景色
            'black'    : 30,   #  黑色
            'red'      : 31,   #  红色
            'green'    : 32,   #  绿色
            'yellow'   : 33,   #  黄色
            'blue'     : 34,   #  蓝色
            'purple'   : 35,   #  紫红色
            'cyan'     : 36,   #  青蓝色
            'white'    : 37,   #  白色
        },

        'back' :
        {   # 背景
            'black'     : 40,  #  黑色
            'red'       : 41,  #  红色
            'green'     : 42,  #  绿色
            'yellow'    : 43,  #  黄色
            'blue'      : 44,  #  蓝色
            'purple'    : 45,  #  紫红色
            'cyan'      : 46,  #  青蓝色
            'white'     : 47,  #  白色
        },

        'mode' :
        {   # 显示模式
            'mormal'    : 0,   #  终端默认设置
            'bold'      : 1,   #  高亮显示
            'underline' : 4,   #  使用下划线
            'blink'     : 5,   #  闪烁
            'invert'    : 7,   #  反白显示
            'hide'      : 8,   #  不可见
        },

        'default' :
        {
            'end' : 0,
        },
}


def use_style(string, fore='', back='', mode=''):
    r'''选择控制台打印文字格式.
    
    :param  string: str, 输出的文字内容.
    :param  fore: str, 文字前景色.
    :param  back: str, 文字背景色.
    :param  back: str, 文字模式, 如是否加粗等.

    :return : str.
    '''

    mode  = '%s' % STYLE['mode'].get(mode, '')
    fore  = '%s' % STYLE['fore'].get(fore, '')
    back  = '%s' % STYLE['back'].get(back, '')
    style = ';'.join([s for s in [mode, fore, back] if s])
    style = '\033[%sm' % style if style else ''
    end   = '\033[%sm' % STYLE['default']['end'] if style else ''
    return '%s%s%s' % (style, string, end)


def test( ):
    print('*'*60)
    print(use_style('正常显示'))
    print('*'*60)

    print("测试前景色")
    print(use_style('黑色',   fore='black'))
    print(use_style('红色',   fore='red'))
    print(use_style('绿色',   fore='green'))
    print(use_style('黄色',   fore='yellow'))
    print(use_style('蓝色',   fore='blue'))
    print(use_style('紫红色', fore='purple'))
    print(use_style('青蓝色', fore='cyan'))
    print(use_style('白色',   fore='white'))
    print('*'*60)

    print("测试背景色")
    print(use_style('黑色',   back='black'))
    print(use_style('红色',   back='red'))
    print(use_style('绿色',   back='green'))
    print(use_style('黄色',   back='yellow'))
    print(use_style('蓝色',   back='blue'))
    print(use_style('紫红色', back='purple'))
    print(use_style('青蓝色', back='cyan'))
    print(use_style('白色',   back='white'))

    print("测试显示模式")
    print(use_style('高亮',   mode='bold'))
    print(use_style('下划线', mode='underline'))
    print(use_style('闪烁',   mode='blink'))
    print(use_style('反白',   mode='invert'))
    print(use_style('不可见', mode='hide'))
    print('*'*60)

    print("测试非正常输入")
    print(use_style('fore非正常输入',   fore='123'))
    print(use_style('back非正常输入', back='123'))
    print(use_style('mode非正常输入',   mode='123'))
    print('*'*60)


if __name__ == '__main__':
    test()