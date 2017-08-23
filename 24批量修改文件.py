#!/usr/bin/env python3
# coding:utf-8

import os
import shutil


def del_folders():
    r'''批量删除非空文件夹.'''

    base_path = '/home/zzzzer/Documents/temp/Projects'
    for root, dirs, files in os.walk(base_path):
        for name in dirs:
            if name == '.vs':
                path = os.path.join(root, name)
                print(path)
                # shutil.rmtree(path)


def recode_files():
    r'''批量修改文件编码.'''

    base_path = '/home/zzzzer/Documents/temp/Projects'
    for root, dirs, files in os.walk(base_path):
        for name in files:
            if name.endswith(('.c', '.h', '.cpp')):
                path = os.path.join(root, name)
                print(path)
                # with open(path, 'rb') as f:
                #     s = f.read()
                # with open(path, 'wb') as f:
                #     f.write(s.decode('gbk').encode())


def tab_to_space():
    r'''批量将文件中的tab转换成4个空格.'''

    base_path = '/home/zzzzer/Documents/temp/Projects'
    for root, dirs, files in os.walk(base_path):
        for name in files:
            if name.endswith(('.c', '.h', '.cpp')):
                path = os.path.join(root, name)
                print(path)
                # with open(path, 'r') as f:
                #     s = f.read()
                # with open(path, 'w') as f:
                #     f.write(s.expandtabs(tabsize=4))


if __name__ == '__main__':
    del_folders()
    #recode_files()
    #tab_to_space()