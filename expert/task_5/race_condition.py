from threading import Thread
import time

global_counter = 0


def incrementer(x):
    global global_counter

    local_counter = global_counter
    local_counter += x
    time.sleep(0.2)
    global_counter = local_counter


if __name__ == '__main__':
    t1 = Thread(target=incrementer, args=(20,))
    t2 = Thread(target=incrementer, args=(80,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"{global_counter=}")


