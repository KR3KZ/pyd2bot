from pyd2bot.clientMain import DofusClient
import json
from time import sleep
import os

ROOTDIR = os.path.dirname(__file__)

c = DofusClient()
conn_f = os.path.join(ROOTDIR, "account.json")

with open(conn_f) as fp:
    conn = json.load(fp)
    
c.start(conn)
c.join()
sleep(10)
c.interrupt()