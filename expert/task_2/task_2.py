import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

def sqr(num):
    print("Calculation square for a number:", num)
    time.sleep(2)
    return num * num

if __name__ == '__main__':
    pool = ThreadPoolExecutor(3)
    sqr1 = pool.submit(sqr, 5)
    sqr2 = pool.submit(sqr, 3)
    sqr3 = pool.submit(sqr, 7)
    sqr4 = pool.submit(sqr, 4)
    sqr5 = pool.submit(sqr, 2)
    sqr6 = pool.submit(sqr, 20)

if sqr1.done():
    print(sqr1.result())


with ThreadPoolExecutor(20) as executor:
    for result in executor.map(sqr, range(20)):
        print(result)


with ThreadPoolExecutor(20) as executor:
    futures = [executor.submit(sqr, i) for i in range(10)]
    for future in as_completed(futures):
        result = future.result()
        print(result)
