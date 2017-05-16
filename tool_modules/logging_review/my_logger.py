#!/usr/local/bin/python
# encoding: utf-8
'''
Created on Jan 22, 2017

@author: Jack

dump_and_pump.my_logger
'''
from logging import NOTSET, INFO, WARNING
from logging.handlers import MemoryHandler
import logging


DEBUG = False

if DEBUG:
    logLevel = NOTSET
    MemoryHandlerCapacity = 10
else:
    logLevel = INFO
    MemoryHandlerCapacity = 1000

# set up logging to file - see previous section for more details
FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# set a format which is simpler for console use
formatter = logging.Formatter(
    '%(asctime)s - %(name)s: %(levelname)s - %(message)s')
formatter_short = logging.Formatter('%(message)s')
debug_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s'
                                    ' - %(message)s --:%(unikey)s')

logging.basicConfig(
    level=WARNING,
    format=FORMAT,
    datefmt='%Y-%m-%d %H:%M',
)
# define a Handler which writes INFO messages or higher to the sys.stderr
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

id_handler = logging.FileHandler("log/detail.log",
                                 mode='w')
id_handler.setLevel(logLevel)

main_formatter = logging.Formatter(FORMAT)
main_handler = logging.FileHandler("log/main.log",
                                   mode='w')
main_handler.setLevel(logLevel)
main_handler.setFormatter(formatter)

result_handler = logging.FileHandler("log/report.log", mode='w')
result_handler.setFormatter(formatter_short)

id_mhandler = MemoryHandler(MemoryHandlerCapacity, target=id_handler)

main_mhandler = MemoryHandler(10, target=main_handler)

result_mhandler = MemoryHandler(1000, target=result_handler)
id_handler.setFormatter(formatter_short)

root_logger = logging.getLogger()
if DEBUG:
    pass
    # add the handler to the root logger
    # logging.getLogger().addHandler(console_handler)
    # logging.getLogger().addHandler(main_mhandler)
    # logging.getLogger().setLevel(logLevel)
else:
    #     logging.getLogger().setLevel(logLevel)
    # root_logger.removeHandler(root_logger.handlers[0])
    pass


# Now, define a couple of other loggers which might represent areas in your
# application:
logger0 = logging.getLogger('myapp')
logger1 = logging.getLogger('myapp.area1')
logger2 = logging.getLogger('myapp.area2')
logger3 = logging.getLogger('myapp.area3')

logger1.addHandler(id_mhandler)
logger2.addHandler(main_handler)
logger3.addHandler(result_mhandler)
# handler01.setLevel(logging.WARNING)
# console_handler.setLevel(logging.WARNING)
# logging.getLogger().setLevel(logging.DEBUG)

if __name__ == '__main__':
    logging.debug("logging.debug")
    logging.info('logging.info')
    logging.warning("logging.warning")

    logger2.debug('logger2.debug')
    logger2.info('logger2.info')
    logger2.warn('logger2.warn')

    logger1.debug('logger1.debug')
    logger1.info('logger1.info')
    logger1.warn("logger1.warn")

    logger3.debug('logger3.debug')
    logger3.info('logger3.info')
    logger3.warn("logger3.warn")

#     logger2.debug('logger2.debug')
#     logger2.warning('logger2.warning')
#     logger2.error('logger2.error')
    pass
