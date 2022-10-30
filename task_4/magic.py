class Magic:
    def __init__(self, num):
        self.my_number = num
        pass

    def __str__(self):
        return f"object STR with number {self.my_number}"

    def __repr__(self):
        return str({"my_number": self.my_number})

    def __add__(self, obj):
        print(type(obj))
        if isinstance(obj, Magic):
            return f"My number now is {self.my_number + obj.my_number}"
        else:
            raise Exception("Cannot add two different objects")


class Sorcery:
    def __int__(self):
        pass


m = Magic(1)
m1 = Magic(2)

print(m+m1)
print(m)
print(repr(m))



