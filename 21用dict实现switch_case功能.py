#!/usr/bin/env python3
# coding: utf-8

"""用dict对象完成switch_case的功能, 以运算符为例."""


# bad
def apply_operation(left_operand, right_operand, operator):
    if operator == '+':
        return left_operand + right_operand
    elif operator == '-':
        return left_operand - right_operand
    elif operator == '*':
        return left_operand * right_operand
    elif operator == '/':
        return left_operand / right_operand


# good
import operator as op
def apply_operation(left_operand, right_operand, operator):
    operator_mapper = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}
    return operator_mapper[operator](left_operand, right_operand)
