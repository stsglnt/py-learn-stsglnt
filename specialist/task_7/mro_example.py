class O:
    def m(self):
        print("O")


class A(O):
    def m(self):
        print("A")


class B(A):
    def m(self):
        print("B")


class C(A, B):
    pass


print(C().m())
print(C.mro())
print(C.__mro__)
print(help(C))



# each ancestor class appears exactly once
# a class always appears before its ancestor ("monotonicity")
# direct parents of the same class should appear in the same order as they are listed in class definition ("consistent local precedence order")
# if children of class A always appear before children of class B, then A should appear before B ("consistent extended precedence order")
