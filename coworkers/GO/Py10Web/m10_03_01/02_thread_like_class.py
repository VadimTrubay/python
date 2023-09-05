from random import randint
from threading import Thread
import logging
from time import sleep


class MyThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args

    def run(self):
        ttl = randint(1, 3)
        sleep(ttl)
        logging.debug(f"In my thread {self.args}: {ttl}s")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    threads = []
    for i in range(5):
        th = MyThread(name=f"Th#{i}", args=(f"Count thread - {i}", ))  # daemon=True
        th.start()
        threads.append(th)

    # [th.join() for th in threads]
    threads[3].join()
    sleep(1)
    logging.debug('End program')
