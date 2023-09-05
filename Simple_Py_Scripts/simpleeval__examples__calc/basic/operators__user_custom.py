#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# SOURCE: https://github.com/danthedeckie/simpleeval#operators


# pip install simpleeval
from simpleeval import SimpleEval

import ast
import operator as op


s = SimpleEval()
s.operators[ast.BitXor] = op.xor
# # OR:
# s.operators[ast.BitXor] = lambda a, b: a ^ b

print(s.eval("2 ^ 10"))  # 8
