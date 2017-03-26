'''
Created on Nov 20, 2016

@author: jack
'''
from queue import Queue
from threading import Lock
import threading
import time

p_lock = Lock()
q = Queue()


def thread_job(worker):
    print("thread_job start")
    time.sleep(1)
    with p_lock:
        print(threading.current_thread())
        time.sleep(1)
    print("thread_job done")


def taskq():
    for i in range(20):
        q.put(i)


def exjob(worker):
#     time.sleep(0.1)
    with p_lock:
        print(threading.current_thread(), "worker: ", worker)


def threader():
    while True:
        worker = q.get()
        exjob(worker)
        q.task_done()


def main():
    for i in range(2):
        thread_name = "Thread- %i" % i
        T = threading.Thread(target=threader,
                             name=thread_name,
                             )
        T.daemon = True
        T.start()


def _main():
#     print(threading.active_count())
#     print(threading.enumerate())
#     print(threading.current_thread())
    for i in range(2):
        thread_name = "Thread- %i" % i
        addT = threading.Thread(target=thread_job,
                                name=thread_name,
                                kwargs={'worker': i})
    addT.daemon = True
    addT.start()
    print(threading.active_count())
    print(threading.enumerate())
    addT.join()
    pass


threading.active_count()

if __name__ == '__main__':
    taskq()
    main()
    pass
