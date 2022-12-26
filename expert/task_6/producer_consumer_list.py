from threading import Thread, Lock
from random import random
from time import sleep


def producer(my_list, my_lock):
    print('Producer: Running')
    my_lock.acquire()
    for i in range(10):
        value = random()
        sleep(value)
        item = (i, value)
        my_list.append(item)
        print(f'producer added {item}')
    lock.release()

    print('Producer: Done')


def consumer(my_list, my_lock):
    print('Consumer: Running')
    my_lock.acquire()
    while len(my_list) > 0:
        item = my_list.pop()
        sleep(item[1])
        print(f'consumer got {item}')
    my_lock.release()
    print('Consumer: Done')


if __name__ == '__main__':
    lock = Lock()
    l = list()
    consumer = Thread(target=consumer, args=(l, lock))
    consumer.start()
    producer = Thread(target=producer, args=(l, lock))
    producer.start()
    producer.join()
    consumer.join()
