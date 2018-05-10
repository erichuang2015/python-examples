#!/usr/bin/env python3
# coding: utf-8


"""第一种方法"""
# import sys
# if len(sys.argv) >= 2:
#     print(sys.argv[1])
# else:
#     print("请输入单词")


"""第二种方法"""
import argparse

# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                    help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                    const=sum, default=max,
#                    help='sum the integers (default: find the max)')

# args = parser.parse_args()
# print(args.accumulate(args.integers))


parser = argparse.ArgumentParser(
        description='Use TUNA mirrors everywhere when applicable')
parser.add_argument(
    'subcommand',
    nargs='?',
    metavar='SUBCOMMAND',
    choices=['up', 'down', 'status'],
    default='up')
parser.add_argument(
    '-v', '--verbose', help='verbose output', action='store_true')
parser.add_argument(
    '-y',
    '--yes',
    help='always answer yes to questions',
    action='store_true')
parser.add_argument(
    '-g',
    '--global',
    dest='is_global',
    help='apply system-wide changes. This option may affect applicability of some modules.',
    action='store_true')

args = parser.parse_args()