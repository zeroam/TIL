"""
It is frequently useful to ignore exceptions raised b libraries, because
the error indicates that the desired state has already been achieved, or
it can otherwise be ignored. The most common way to ignore exceptions is
with a try:except statement with only a pass statement in the except block
"""
import contextlib


class NonFatalError(Exception):
    pass


def non_idempotent_operation():
    raise NonFatalError(
        'The operation failed because of existing state'
    )


try:
    print('trying non-idempotent operation')
    non_idempotent_operation()
    print('succeed!')
except NonFatalError:
    pass

print('done')
