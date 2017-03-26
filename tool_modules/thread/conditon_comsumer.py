#!/usr/bin/env python
# encoding: utf-8
'''
Created on Mar 26, 2017

@author: Jack
'''
import threading


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
        threading.Thread.__init__(self)
        self.integers = integers
        self.condition = condition


def run(self):
    """
    实现Thread的run()方法，从列表中消费整数
    """
    while True:
        self.condition.acquire()  # 获取条件锁
        print('condition acquired by %s' % self.name)
        while True:
            if self.integers:  # 判断是否有整数
                integer = self.integers.pop()
                print('%d popped from list by %s' % (integer, self.name))
                break
                print('condition wait by %s' % self.name)
                self.condition.wait()  # 等待商品，并且释放资源
                print('condition released by %s' % self.name)
                self.condition.release()  # 最后释放条件锁


if __name__ == '__main__':
    c = Consumer()
    pass
