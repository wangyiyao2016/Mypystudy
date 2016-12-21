'''
Created on Dec 21, 2016

@author: jack
'''
import glob
import logging
from logging import handlers


filename = "log/test.log"

logger = logging.getLogger("MyLogger")

logger.setLevel(logging.DEBUG)

handler = handlers.RotatingFileHandler(filename,
                                       maxBytes=10**4,
                                       backupCount=10,
                                       )
logger.addHandler(handler)


def run(logger):
    for i in xrange(10**2):
        logger.debug("i = %d" % i)

    log_files = glob.glob("%s*" % filename)
    for i in log_files:
        print i

if __name__ == '__main__':
    run(logger)
