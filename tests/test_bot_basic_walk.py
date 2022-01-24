import json
from time import perf_counter, sleep
from pyd2bot.bot import Bot
import os
ROOTDIR = os.path.dirname(__file__)
bot = Bot()
conn_f = os.path.join(ROOTDIR, "account.json")

with open(conn_f) as fp:
    conn = json.load(fp)
    
bot.start(conn)
bot.connectToLoginServer()
bot.inGame.wait()
bot.gameContextCreate()
bot.onMap.wait()
bot.requestMapData()
bot.mapDataReceived.wait()
bot.walkToCell(144)
bot.idle.wait()
print("bot stopped moving")
bot.interrupt()