#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing.managers import BaseManager
import queue
import time


class QueueManager(BaseManager):
    pass


QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr = '127.0.0.1'
m = QueueManager(address=(server_addr, 5000), authkey=b'123')
m.connect()
print('Connect to server %s...' % server_addr)
task = m.get_task_queue()
result = m.get_result_queue()
while True:
    try:
        n = task.get(timeout=3)
    except queue.Empty:
        print('task queue is empty.')
        break
    else:
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(0)
        result.put(r)
print('worker exit.')
