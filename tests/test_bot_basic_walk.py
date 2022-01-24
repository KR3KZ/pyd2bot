import json
from pyd2bot.bot import Bot
import os

ROOTDIR = os.path.dirname(__file__)
creds_f = os.path.join(ROOTDIR, "account.json")
with open(creds_f) as fp:
    creds = json.load(fp)

from pyd2bot.bot import Bot
creds = {
    "login": "kmajdoub",
    "password": "rMrTXHA4*",
    "name": "John-shooter",
    "serverID": 210
}
bot = Bot(**creds)    
bot.login()
bot.collect()
bot.disconnect()