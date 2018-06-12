#!/usr/bin/env python
'''
Created on Jun 12, 2018
'''
from multiprocessing.managers import BaseManager
import queue


class QueueManager(BaseManager):
    pass


def main():
    task_queue = queue.Queue()
    result_queue = queue.Queue()
    QueueManager.register('get_task_queue', callable=lambda: task_queue)
    QueueManager.register('get_result_queue', callable=lambda: result_queue)
    with QueueManager(address=('127.0.0.1', 5000), authkey=b'123') as manager:
        result = manager.get_result_queue()
        print('server running.')
        while True:
            try:
                r = result.get()
            except queue.Empty:
                break
            else:
                print('Result: %s' % r)


if __name__ == '__main__':
    main()
    pass
