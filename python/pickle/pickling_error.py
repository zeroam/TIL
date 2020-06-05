import pickle

square = lambda x: x * x
# pickle module can't serialize a lambda function
my_pickle = pickle.dumps(square)
