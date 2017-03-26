#!/usr/bin/env python
# encoding: utf-8
'''
Created on Mar 26, 2017

@author: Jack
'''
import random
import threading
import time

p_lock = threading.Lock()
cv = threading.Condition(p_lock)


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
        threading.Thread.__init__(self)
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
            time.sleep(1)  # 暂停1秒钟


if __name__ == '__main__':
    int_list = list(range(10))
    p = Producer(int_list, cv)
    p.run()
    pass
