#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing.managers import BaseManager
import random


class QueueManager(BaseManager):
    pass


QueueManager.register('get_task_queue')

server_addr = '127.0.0.1'
m = QueueManager(address=(server_addr, 5000), authkey=b'123')
m.connect()
print('Connect to server %s...' % server_addr)


def main():
    task_queue = m.get_task_queue()
    for _ in range(100):
        n = random.randint(5000, 10000)
        print('Put task %d...' % n)
        task_queue.put_nowait(n)
    print('mapper exit.')


if __name__ == '__main__':
    main()
    pass
