# https://www.careercup.com/question?id=4783236498587648

import threading
import time

cv1 = threading.Condition()
cv2 = threading.Condition()
cv3 = threading.Condition()

LIMIT = 10


class myThread(threading.Thread):
    def __init__(self, lock1, lock2):
        threading.Thread.__init__(self)
        self.lock1 = lock1
        self.lock2 = lock2

    def run(self):
        with self.lock1:
            self.lock1.notify()
        with self.lock2:
            self.lock2.notify()

        for i in range(LIMIT):
            with self.lock1:
                self.lock1.wait()
            print self.name
            with self.lock2:
                self.lock2.notify()




if __name__ == '__main__':
    t1 = myThread(cv1, cv2)
    t2 = myThread(cv2, cv3)
    t3 = myThread(cv3, cv1)

    t1.start()
    t2.start()
    t3.start()
