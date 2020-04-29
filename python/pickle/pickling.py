import pickle


class example_class:
    a_number = 35
    a_string = "hey"
    a_list = [1, 2, 3]
    a_dict = {"first": "a", "second": 2, "third": [1, 2, 3]}
    a_tuple = (22, 23)


my_object = example_class()

my_pickle_object = pickle.dumps(my_object)  # Picking the object
print(f"This is my pickle object:\n{my_pickle_object}\n")

my_object.a_dict = None

my_unpickled_object = pickle.loads(my_pickle_object)  # Unpicking the object
print(f"This is a dict of the unpickled object:")
print(my_unpickled_object.a_dict)
