import atexit


@atexit.register
def all_done():
    print('all_done()')


print('starting main program')
