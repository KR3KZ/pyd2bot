import json
from time import perf_counter, sleep
from pyd2bot.logic.bot.bot import Bot
import os

from pyd2bot.logic.common.managers.mapManager import MapManager
from pyd2bot.logic.common.managers.playerManager import PlayerManager


ROOTDIR = os.path.dirname(__file__)

bot = Bot()
conn_f = os.path.join(ROOTDIR, "account.json")

with open(conn_f) as fp:
    conn = json.load(fp)
    
bot.start(conn)

bot.connectToLoginServer()
PlayerManager.inGame.wait()
bot.gameContextCreate()
PlayerManager.onMap.wait()
bot.requestMapData()
sleep(1)
bot.walkToCell()
sleep(3)
bot.interrupt()