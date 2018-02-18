import threading

class BlockingQueue:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.mutex = threading.Lock()
        self.not_full = threading.Condition(self.mutex)
        self.not_empty = threading.Condition(self.mutex)
        self.store = []

    def put(self, value):
        with self.not_full:
            while len(self.store) == self.maxsize:
                self.not_full.wait()
            self.store.append(value)
            self.not_empty.notify()

    def get(self):
        with self.not_empty:
            while len(self.store) == 0:
                self.not_empty.wait()
            popped = self.store.pop(0)
            self.not_full.notify()
            return popped


if __name__ == '__main__':
    q = BlockingQueue(3)
    q.put(1)
    q.put(2)
    print q.get()
    q.put(3)
    q.put(4)
