import functools

@functools.lru_cache
def fib(n):
    if n <= 1:
        return n
    else:
        print("calculation n", n)
        return fib(n - 1) + fib(n - 2)

