from pyd2bot.logic.auth.authentificationManager import ROOTDIR
from pyd2bot.network.client import DofusClient
import json
from time import sleep
import os

ROOTDIR = os.path.dirname(__file__)

c = DofusClient()
creds_f = os.path.join(ROOTDIR, "account.json")
with open(creds_f) as fp:
    auth_json = json.load(fp)
    c._login = auth_json["username"]
    c._password = auth_json["password"]
c.start()
c.join()
sleep(10)
c.interrupt()