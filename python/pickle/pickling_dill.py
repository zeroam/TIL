import dill

square = lambda x: x * x
my_pickle = dill.dumps(square)
print(my_pickle)
