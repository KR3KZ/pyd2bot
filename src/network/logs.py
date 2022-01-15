import logging

FORMAT = "%(asctime)s %(levelname)s | %(threadName)s - [%(pathname)s:%(lineno)d] in %(funcName)s | \n%(message)s\n"
logging.basicConfig(format=FORMAT, filename="labot.log", encoding='utf-8', level=logging.DEBUG, filemode="w")