#!/usr/bin/env python
# encoding: utf-8
'''
Created on Mar 26, 2017

@author: Jack
'''
from queue import Queue
import threading
import time


print_lock = threading.Lock()


def exampleJob(worker):
    # time.sleep(1)  # pretend to do some work.
    with print_lock:
        time.sleep(1)
        ct = threading.current_thread()
        print(ct, ct.name, worker)
        time.sleep(1)


# The threader thread pulls an worker from the queue and processes it
def threader():
    while True:
        # gets an worker from the queue
        worker = q.get()

        # Run the example job with the avail worker in queue (thread)
        exampleJob(worker)

        # completed with the job
        q.task_done()


# Create the queue and threader
q = Queue()

# how many threads are we going to allow for
for x in range(4):
    t = threading.Thread(target=threader)

    # classifying as a daemon, so they will die when the main dies
    t.daemon = True

    # begins, must come after daemon definition
    t.start()

start = time.time()

# 20 jobs assigned.
for worker in range(4):
    q.put(worker)

# wait until the thread terminates.
q.join()

# with 10 workers and 20 tasks, with each task being .5 seconds, then the completed job
# is ~1 second using threading. Normally 20 tasks with .5 seconds each would take 10 seconds.
print('Entire job took:', time.time() - start)


if __name__ == '__main__':
    pass
