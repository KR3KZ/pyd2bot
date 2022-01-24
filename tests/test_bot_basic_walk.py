import json
from pyd2bot.bot import Bot
import os

ROOTDIR = os.path.dirname(__file__)
creds_f = os.path.join(ROOTDIR, "account.json")
with open(creds_f) as fp:
    creds = json.load(fp)

bot = Bot(**creds)    
bot.login()
bot.walkToCell(311)
bot.disconnect()