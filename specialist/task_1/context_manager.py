from threading import Lock
from contextlib import contextmanager

class MyLockContextManager:
    def __init__(self):
        self.lock = Lock()

    def __enter__(self):
        self.lock.acquire()
        return

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.lock.release()

@contextmanager
def my_lock_context_manager():
    lock = Lock()
    lock.acquire()
    yield
    lock.release()

if __name__ == "__main__":
    my_list = []
    with MyLockContextManager():
        my_list.append("New Value")
        print(my_list)

    my_list2 = []
    with my_lock_context_manager():
        my_list2.append("New Value")
