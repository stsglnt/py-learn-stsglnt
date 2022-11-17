import pickle


class ExampleClass:
    def __init__(self):
        self.my_string = "My String Value"
        self.my_list = ["First", "Second", "Third"]


example_instance = ExampleClass()
with open("example.pickle", "wb") as example_pickle_file:
    pickle.dump(example_instance, example_pickle_file)

with open("example.pickle", "rb") as example_pickle_file:
    p = pickle.load(example_pickle_file)

example_instance.my_list = "My Modified List"

print("my_pickle", p.my_string)
