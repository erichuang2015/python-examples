#!/usr/bin/env python3
# coding:utf-8


"""第一种方法"""
# import sys
# if len(sys.argv) >= 2:
#     print(sys.argv[1])
# else:
#     print("请输入单词")


"""第二种方法"""
import argparse

parser = argparse.ArgumentParser(description='Search some files')