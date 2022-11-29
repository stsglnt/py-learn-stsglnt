import time


def execution_time(f):
    def wrapper(*args):
        before = time.time()
        v = f(*args)
        print(f"Execution time: {time.time() - before} secs")
        return v
    return wrapper


@execution_time
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":

    print("fibonacci", fib(6))

