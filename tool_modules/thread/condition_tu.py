#!/usr/bin/env python
# encoding: utf-8
'''
Created on Mar 26, 2017

@copied_by: Jack
'''
import random
import threading
import time
import logging


class Producer(threading.Thread):
    """
      向列表中生产随机整数
    """

    def __init__(self, integers, condition):
        """
        构造器
        @param integers 整数列表
        @param condition 条件同步对象
        """
        super().__init__()
        self.integers = integers
        self.condition = condition

    def run(self):
        """
        实现Thread的run方法。在随机时间向列表中添加一个随机整数
        """
        while True:
            integer = random.randint(0, 256)
            self.condition.acquire()  # 获取条件锁
            print('condition acquired by %s' % self.name)
            self.integers.append(integer)
            print('%d appended to list by %s' % (integer, self.name))
            print('condition notified by %s' % self.name)
            self.condition.notify()  # 唤醒消费者线程
            print('condition released by %s' % self.name)
            self.condition.release()  # 释放条件锁
            time.sleep(5)  # 暂停1秒钟


class Consumer(threading.Thread):
    """
      从列表中消费整数
    """

    def __init__(self, integers, condition):
        """
        构造器

        @param integers 整数列表
        @param condition 条件同步对象
        """
        super().__init__()
        self.integers = integers
        self.condition = condition

    def run(self):
        """
        实现Thread的run()方法，从列表中消费整数
        """
#         while True:
        with self.condition:  # 获取条件锁
            print('condition acquired by %s' % self.name)
            while self.integers:
                print("len: ", len(self.integers))
                integer = self.integers.pop()
                print('%d popped from list by %s' % (integer, self.name))
            self.condition.wait()  # 等待商品，并且释放资源
            print('condition wait by %s' % self.name)
        print('condition released by %s' % self.name)
        # time.sleep(1)


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - (%(threadName) -2s %(message)s)'
)


def consumer(cond):
    #     t = threading.current_thread()
    logging.debug('Starting consumer thread')
    with cond:
        logging.debug('consumer begin to wait')
        cond.wait()
        logging.debug('res available to consumer')


def producer(cond):
    logging.debug('Starting producer thread')
    with cond:
        logging.debug('Make res available to consumers')
#         cond.notify_all()
#         logging.debug('notify_all done')
        cond.notify(n=1)
        logging.debug('notify one thread')


def main():
    integers = []
    condition = threading.Condition()
    t1 = Producer(integers, condition)
    t2 = Consumer(integers, condition)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def test():
    condition = threading.Condition()
    c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
    c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
    p1 = threading.Thread(name='p1', target=producer, args=(condition,))
    p2 = threading.Thread(name='p2', target=producer, args=(condition,))
    c1.start()
    time.sleep(2)
    c2.start()
    time.sleep(2)
    p1.start()
    time.sleep(2)
    p2.start()


if __name__ == '__main__':
    test()
    pass
