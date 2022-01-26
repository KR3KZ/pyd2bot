import json
from pyd2bot.bot import Walker
from pyd2bot.network import MsgListner
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

try:
    bot = Walker(**creds)
    if bot.login():
        for _ in range(100):
            bot.randWalk()
        bot.disconnect()
except Exception as e:
    bot.disconnect()
    raise e
    