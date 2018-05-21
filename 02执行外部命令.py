#!/usr/bin/env python3
# coding: utf-8

"""subprocess 模块对于依赖 TTY 的外部命令不合适用."""

import subprocess


def print_lib():
    """打印已安装的第三方库, pip版本 10.x."""

    # check_output() 中,
    # 通常来讲, 命令的执行不需要使用到底层 shell 环境(比如 sh, bash)
    # 一个字符串列表会被传递给一个低级系统命令, 比如 os.execve()
    # 如果你想让命令被一个 shell 执行, 传递一个字符串参数, 并设置参数 shell=True
    # 这样就可以执行一些复杂的命令, 如管道
    # 默认不输出stderr的内容, `stderr=subprocess.STDOUT`参数, 将stderr输出到stdout
    # timeout 参数可设置超时时间, 单位秒
    output_bytes = subprocess.check_output(['pip3', 'list'], stderr=subprocess.STDOUT)
    output_text = output_bytes.decode('utf-8').strip()
    lib_list = output_text.split('\n')[2:]
    for lib in lib_list:
        # 只打印库名, 不打印版本
        print(lib.split()[0], end=' ')
    print()


def command_arg():
    """给外部命令传参的方法.
    
    把一段文字传给 wc 命令.
    """

    text = b'hello world, this is a test, goodbye.'
    p = subprocess.Popen(['wc'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout, stderr = p.communicate(text)
    if stdout:
        print(stdout.decode('utf-8'))
    if stderr:
        print(stderr.decode('utf-8'))


if __name__ == '__main__':
    print_lib()
    #command_arg()
