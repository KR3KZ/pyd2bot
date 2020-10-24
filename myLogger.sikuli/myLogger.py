import logging
import datetime as dt

global logger
logger = logging.getLogger("logger")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fmt = '%(lineno)s %(threadName)s %(message)s'
formatter = logging.Formatter(fmt)
ch.setFormatter(formatter)
logger.addHandler(ch)

print('logger loaded')
