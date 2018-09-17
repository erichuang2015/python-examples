#!/usr/bin/env python3
# coding: utf-8

"""在内存中读取数据。

相关的应用是：
PIL 的 `Image.open()` 是不能直接打开 b'xxxx' 形式的内容的，
需要先令 `f = BytesIO(b'xxxx')` 转换格式，再用 `Image.open(f)` 打开
"""

from io import StringIO, BytesIO


def main():
    """内存中写字符串"""
    with StringIO() as f:
        f.write('hello')
        f.write(' world')
        # 取出值
        print(f.getvalue())
    # 或者
    with StringIO('hello world') as f:
        print(f.getvalue())

    """内存中写字节流（操作跟 StringIO 一致，只是要传入字节流）"""
    with BytesIO() as f:
        f.write('hello'.encode())
        f.write(' world'.encode())
        print(f.getvalue())
    # 或者
    with BytesIO('hello world'.encode()) as f:
        print(f.getvalue())


if __name__ == '__main__':
    main()
