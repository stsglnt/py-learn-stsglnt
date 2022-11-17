def is_exist_key(keys, dictionary):
    return all(key in keys for key in dictionary)

class AllType:
    my_str = 'My string value'
    my_number = 100
    my_list = [1, 2, 3, 4, "some string", (1, 2)]
    my_dict = dict(key_1="value_1", key_2="value_2")
    my_set = {1, 2, 3, 4}

    def __int__(self):
        pass

    # str
    def str_replace(self, from_value, to_value):
        if isinstance(from_value, str) and isinstance(to_value, str):
            self.my_str = self.my_str.replace(from_value, to_value)
        else:
            raise TypeError('Arguments should be of type string')

    # num
    def num_add(self, value_to_add):
        limit = 10000
        if not isinstance(value_to_add, (int, float)):
            raise TypeError('Arguments should be flot or int')
        elif value_to_add > limit:
            raise ValueError(f"Number should not be bigger than {limit}")
        else:
            self.my_number += value_to_add

    # list
    def list_append(self, value_to_append):
        self.my_list.append(value_to_append)

    def list_delete(self, to_delete):
        if isinstance(to_delete, int) and not isinstance(to_delete, bool):
            if self.my_list[to_delete]:
                del self.my_list[to_delete]
            else:
                raise IndexError
        elif isinstance(to_delete, str):
            if to_delete in self.my_list:
                self.my_list.remove(to_delete)
            else:
                raise ValueError("Such string doesn't exist")
        elif isinstance(to_delete, tuple):
            if to_delete in self.my_list:
                self.my_list.pop(self.my_list.index(to_delete))
            else:
                raise ValueError("Such tuple doesn't exist")
        else:
            raise TypeError("Arguments should be int, str or tuple")

    # dict
    def dict_update(self, *args, **kwargs):
        for arg in args:
            if isinstance(arg, dict):
                if is_exist_key(arg, self.my_dict):
                    self.my_dict.update(arg)
                else:
                    raise ValueError("One of the key doesn't not exist in the dict")
            else:
                raise TypeError("Positional arguments should be of type dict")
        if kwargs:
            self.my_dict.update(kwargs)

    # set
    def set_remove(self, value_to_remove):
        if value_to_remove in self.my_set:
            self.my_set.discard(value_to_remove)
        else:
            raise ValueError("Value doesn't exist in the set")


all_type = AllType()

# string method
try:
    all_type.str_replace("My", "A")
except TypeError as e:
    print(e)
except Exception as e:
    print(e)

# num method
try:
    all_type.num_add(True)
except TypeError as e:
    print(e)
except Exception as e:
    print(e)

# list methods
all_type.list_append("string value")
all_type.list_append((1, 2, 3))

try:
    all_type.list_delete(1)
except IndexError as e:
    print(e)
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
except Exception as e:
    print(e)

# dict
try:
    all_type.dict_update({"key_1": "value_1_update", "key_3": "value_3"}, key_2="value_2_updated")
except Exception as e:
    print(e)

# set
try:
    all_type.set_remove(1)
except Exception as e:
    print(e)

print()
print(f"{all_type.my_str=}\n"
      f"{all_type.my_number=}\n"
      f"{all_type.my_list}\n"
      f"{all_type.my_dict}\n"
      f"{all_type.my_set}")
