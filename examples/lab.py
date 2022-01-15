import atexit
import datetime
import os
import time
from core.bot import Walker
from core import env
import logging 

work_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(work_dir, 'bot.log')
logging.basicConfig(filename=log_file,
                    level=logging.DEBUG,
                    format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d:%H:%M:%S')

myBot = Walker(work_dir)
myBot.sniffer.start()
time.sleep(2)
env.focusDofusWindow()
myBot.getCurrPos()
myBot.moveToMap((-17, -47))
        