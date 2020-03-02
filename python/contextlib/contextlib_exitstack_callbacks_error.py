"""
The callbacks are invoked regardless of whether an error occurred, and
they are not given any information about whether an error occurred.
Their return value is ignored.
"""
import contextlib


def callback(*args, **kwargs):
    print('closing callback({}, {})'.format(args, kwargs))


try:
    with contextlib.ExitStack() as stack:
        stack.callback(callback, 'arg1', 'arg2')
        stack.callback(callback, arg3='val3')
        raise RuntimeError('thrown error')
except RuntimeError as err:
    print('ERROR: {}'.format(err))
