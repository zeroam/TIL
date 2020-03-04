import atexit


def my_cleanup(name):
    print('my_cleanup({})'.format(name))


if False:
    atexit.register(my_cleanup, 'never registered')
    
# Removing a callback that was not previously registered is not considered an error
atexit.unregister(my_cleanup)
