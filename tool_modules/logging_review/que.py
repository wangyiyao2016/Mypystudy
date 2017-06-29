#!/usr/local/bin/python
# encoding: utf-8
'''
Created on Jun 28, 2017

@author: Jack

tool_modules.logging_review.que is a description

@contact:    wangzhijie@bbdservice.com
'''
from logging.handlers import QueueHandler
from queue import Queue

queue_obj = Queue()
que_handler = QueueHandler(queue_obj)

if __name__ == '__main__':
    print(queue_obj)
    pass
