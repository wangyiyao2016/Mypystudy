#!/usr/local/bin/python
# encoding: utf-8
'''
Created on Feb 9, 2017

@author: Jack

tool_modules.logging_review.logging_level_inheritance

@contact:    wangzhijie@bbdservice.com
'''
import logging

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s'
                              ' - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


def test():
    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')


if __name__ == '__main__':
    test()
    pass
