import traceback


class MyClass:
    my_value1 = 1
    my_value2 = 2

    def __init__(self):
        self.my_value3 = 3

    def my_method(self):
        pass


my_instance = MyClass()

print(dir(my_instance))
print(vars(my_instance))
print("dict", my_instance.__dict__)


def my_func():
    try:
        raise Exception("oops")
    except Exception:
        traceback.print_stack()


if __name__ == "__main__":
    my_func()
