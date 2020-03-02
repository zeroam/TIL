"""
The class ContextDecorator adds support to regular context manager classes
to let them be used as function decorators as well as context manager.
"""

import contextlib


class Context(contextlib.ContextDecorator):

    def __init__(self, how_used):
        self.how_used = how_used
        print('__init__({})'.format(how_used))

    def __enter__(self):
        print('__enter__({})'.format(self.how_used))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__({})'.format(self.how_used))


@Context('as decorator')
def func(message):
    print(message)

print()
with Context('as content manager'):
    print('Doing work in the context')

print()
func('Doing work in the wrapped function')