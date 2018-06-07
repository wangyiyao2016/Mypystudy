#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing.managers import BaseManager
import queue
import random

task_queue = queue.Queue()
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass


QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

with QueueManager(address=('127.0.0.1', 5000), authkey=b'123') as manager:
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    for i in range(30):
        n = random.randint(5000, 10000)
        print('Put task %d...' % n)
        task.put_nowait(n)
    while True:
        try:
            r = result.get(timeout=6)
        except queue.Empty:
            break
        else:
            print('Result: %s' % r)
print('master exit.')
