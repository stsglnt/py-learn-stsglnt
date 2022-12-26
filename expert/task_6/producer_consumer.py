from threading import Thread
from queue import Queue
from random import random
from time import sleep


def producer(q):
    print('Producer: Running')
    for i in range(10):
        value = random()
        sleep(value)
        item = (i, value)
        q.put(item)
        print(f'producer added {item}')
    q.put(None)
    print('Producer: Done')


def consumer(q):
    print('Consumer: Running')
    while True:
        item = q.get()
        if item is None:
            break
        sleep(item[1])
        print(f'consumer got {item}')
    print('Consumer: Done')


if __name__ == '__main__':
    queue = Queue()
    consumer = Thread(target=consumer, args=(queue,))
    producer = Thread(target=producer, args=(queue,))
    consumer.start()
    producer.start()
    producer.join()
    consumer.join()
