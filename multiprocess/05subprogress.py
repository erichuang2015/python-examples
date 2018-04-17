#!/usr/bin/env python3
# coding:utf-8

"""
subprocess 模块可以让我们非常方便地启动一个子进程，
然后控制其输入和输出.
"""

import subprocess


# 下面的例子演示了如何在 Python 代码中运行命令 
# nslookup www.python.org
# 这和命令行直接运行的效果是一样的
def nslookup():
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)


# 如果子进程还需要输入，则可以通过 communicate() 方法输入
# 下面的代码相当于在命令行执行命令 nslookup ，然后手动输入：
# set q=mx
# python.org
# exit
def input_():
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('gbk'))
    print('Exit code:', p.returncode)


if __name__ == '__main__':
    input_()