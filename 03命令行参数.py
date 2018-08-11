#!/usr/bin/env python3
# coding: utf-8


"""第一种方法."""
# import sys
# if len(sys.argv) >= 2:
#     print(sys.argv[1])
# else:
#     print("请输入单词")


"""第二种方法."""
import argparse


def arg_parse():
    """模拟mysql命令行参数。

    add_argument() 各个参数含义：
    name/flags：参数的名字
    action：遇到参数时的动作，默认值是 store。
            store，常规储存一个值，类型根据 type 决定
            store_true，表示那种没有值的额外参数
            store_const，表示赋值为 const
            append，将遇到的值存储成列表, 也就是如果参数重复则会保存多个值
            append_const，将参数规范中定义的一个值保存到一个列表
            count，存储遇到的次数；此外，也可以继承 argparse.Action 自定义参数解析
    nargs：参数的个数，可以是具体的数字。
           或 '+'，代表1个或多个参数
           或 '*'，代表0个或多个参数
           或 '?'，代表0个或一个参数
    choices：参数可允许的值的一个列表
    default：不指定参数时的默认值
    type：参数的类型，默认应该 str
    required：参数是否可以被省略
    dest：解析后参数的变量名，不指定时是参数的名称
    help：参数的帮助信息
    metavar：在 usage 说明中，参数的名称，不指定时是 dest 的内容大写

    不加'-'或'--', 代表这是个不需要指定参数的值，但同时这个值必须有
    """

    parser = argparse.ArgumentParser(description='A Python-MySQL client')

    parser.add_argument(
        'host',
        metavar='HOST',
        help='connect to host'
    )
    parser.add_argument(
        '-u',
        '--user',
        dest='user',  # dest 其实可以不指定，自动根据上面最长的 key 生成
        required=True,
        help='user for login'
    )
    parser.add_argument(
        '-p',
        '--password',
        dest='password',
        required=True,
        help='password to use when connecting to server'
    )
    parser.add_argument(
        '-P',
        '--port',
        dest='port',
        default='3306',
        type=int,
        help='port number to use for connection or 3306 or default'
    )
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 0.1'
    )
    # 实现那种-v输出详细内容, -vv输出更详细内容的功能
    parser.add_argument(
        '-v',
        '--verbose',
        action='count',
        default=0,  # 这里的default不能不指定, 否则是None
        help='increase output verbosity'
    )
    # 实现不需要指定值的参数功能
    # 不指定时, 该值默认是False, 所以不用再设置default参数
    parser.add_argument(
        '-d',
        dest='daemon',
        choices=['start', 'stop', 'restart'],
        help='whether daemon'
    )
    return parser.parse_args()


def main():
    parser = arg_parse()
    conn_args = dict(
        host=parser.host,
        user=parser.user,
        password=parser.password,
        port=parser.port
    )
    print(conn_args)
    print(parser.verbose)
    print(parser.daemon)


if __name__ == '__main__':
    main()
