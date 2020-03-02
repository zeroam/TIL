"""
Creating context managers the traditional way, by writing a class with
__enter__() and __exit__() methods, is not difficult.
But sometimes writing everything out fully is extra overhead for a
trivial bit of context. In those sorts of situations, use the contextmanager()
decorator to convert a generator function into a context manager.
"""
import contextlib


@contextlib.contextmanager
def make_context():
    print('  entering')
    try:
        yield {}
    except RuntimeError as err:
        print('  ERROR:', err)
    finally:
        print('  exiting')


print('Normal:')
with make_context() as value:
    print('  inside with statement:', value)

print('\nHandled error:')
with make_context() as value:
    raise RuntimeError('showing example of handling an error')

print('\nUnhandled error:')
with make_context() as value:
    raise ValueError('this exception is not handled')
