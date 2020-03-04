"""
The following simple example demonstarates how a module can initialize a counter from a file
when it is imported and save the counter's updated value automatically when the program terminates
without relying on the application making an explicit call into this module at termination
"""
try:
    with open("counterfile") as infile:
        _count = int(infile.read())
except FileNotFoundError:
    _count = 0

def incrcounter(n):
    global _count
    _count = _count + n

def savecounter():
    with open('counterfile', 'w') as outfile:
        outfile.write('%d' % _count)


import atexit
atexit.register(savecounter)


"""
Positional and keyword arguments may also be passwd to `register()`
"""
def goodbye(name, adjective):
    print('Goodbye, %s, it was %s to meet you.' % (name, adjective))

# Positinoal arguments
atexit.register(goodbye, 'Denny', 'nice')
# Keyword arguments
atexit.register(goodbye, adjective='nice', name='Donny')


"""
Usage as a decorator
"""
@atexit.register
def goodbye2():
    print('You are now leaving the Python selector')