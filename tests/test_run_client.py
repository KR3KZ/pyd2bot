from pyd2bot.network.client import DofusClient
import json
from time import sleep
import os

ROOTDIR = os.path.dirname(__file__)

c = DofusClient()
creds_f = os.path.join(ROOTDIR, "account.json")
conn = {}
with open(creds_f) as fp:
    auth_json = json.load(fp)
    conn["login"] = auth_json["username"]
    conn["password"] = auth_json["password"]
    conn["serverID"] = 210
c.start(conn)
c.join()
sleep(10)
c.interrupt()