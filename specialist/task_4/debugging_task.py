import functools
import cProfile
import pstats


@functools.lru_cache
def fib(n):
    if n <= 1:
        return n
    else:
        print("calculation n", n)
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    fib(10)

    cProfile.run("fib(55)", "output.dat")

with open("output_time.txt", "w") as f:
    p = pstats.Stats("output.dat", stream=f)
    p.sort_stats("time").print_stats()

with open("output_calls.txt", "w") as f:
    p = pstats.Stats("output.dat", stream=f)
    p.sort_stats("calls").print_stats()
