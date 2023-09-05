#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# SOURCE: https://github.com/danthedeckie/simpleeval/blob/master/README.rst#extending


# pip install simpleeval
import simpleeval
import ast


class EvalNoMethods(simpleeval.SimpleEval):
    def _eval_call(self, node):
        if isinstance(node.func, ast.Attribute):
            raise simpleeval.FeatureNotAvailable("No methods please, we're British")

        return super()._eval_call(node)


if __name__ == '__main__':
    class Foo:
        @classmethod
        def get(cls):
            return 1

    my_eval = simpleeval.SimpleEval()
    my_eval.names['foo'] = Foo

    print(my_eval.eval('"hello".upper()'))  # HELLO
    print(my_eval.eval('foo.get()'))        # 1
    print()

    # Disable object methods
    my_eval_no_methods = EvalNoMethods()
    my_eval_no_methods.names['foo'] = Foo

    try:
        print(my_eval_no_methods.eval('"foo".upper()'))
    except Exception as e:
        print(e)  # No methods please, we're British

    try:
        print(my_eval_no_methods.eval('foo.get()'))
    except Exception as e:
        print(e)  # No methods please, we're British
