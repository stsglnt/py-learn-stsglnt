class FibIter:

    def __init__(self, max_iter=100):
        self.a, self.b = 0, 1
        self.max = max_iter

    def __iter__(self):
        return self

    def next(self):
        if self.a > self.max:
            raise StopIteration
        value_to_be_returned = self.a
        self.a, self.b = self.b, self.a + self.b
        return value_to_be_returned

    def __next__(self):
        return self.next()


def fib_gen(max_iter=150):
    a, b = 0, 1
    while a < max_iter:
        yield a
        a, b = b, a+b


if __name__ == "__main__":

    fib_numbers = FibIter(150)
    for fib_number in fib_numbers:
        print("fib iter:", fib_number)

    for fib_number in fib_gen():
        print("fib gen:", fib_number)
