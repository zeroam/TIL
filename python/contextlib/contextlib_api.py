class Context:

    def __init__(self):
        print('__init__()')

    def __enter__(self):
        print('__enter__()')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__()')


with Context():
    print('Doing work in the context')