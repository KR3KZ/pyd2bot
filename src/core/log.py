import logging


def joinArgs(args):
    return ', '.join(map(str, args))


class Log:
    def __init__(self):
        format = "<%(asctime)-15s %(levelname)s line %(lineno)d %(threadName)s> %(funcName)s: %(message)s"
        logging.basicConfig(level=logging.INFO, format=format)
        self.log = logging.getLogger("bot logger")

    def info(self, *args):
        self.log.info(joinArgs(args))

    def debug(self, *args):
        self.log.debug(joinArgs(args))

    def error(self, *args, **kwargs):
        self.log.error(joinArgs(args), kwargs)
