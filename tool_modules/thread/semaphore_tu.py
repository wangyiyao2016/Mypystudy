'''
Created on Nov 22, 2017
'''
import threading
import time
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - (%(threadName) -2s %(message)s)'
)


class ActivePool:
    def __init__(self):
        super().__init__()
        self.active = list()
        self.lock = threading.Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug('Runing:  %s', self.active)

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug('Runing: %s', self.active)


def worker(s, pool):
    logging.debug('Waiting to join the pool')
    with s:
        logging.debug('get s lock')
        name = threading.current_thread().name
        pool.makeActive(name)
        time.sleep(5)
        pool.makeInactive(name)


if __name__ == '__main__':
    pool = ActivePool()
    s = threading.Semaphore(2)
    for i in range(1, 5):
        t = threading.Thread(target=worker,
                             name=str(i),
                             args=(s, pool))
        t.start()
    pass
