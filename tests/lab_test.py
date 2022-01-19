import socket
from pyd2bot.core.network.sniffer.dofusSniffer import DofusSniffer
from pyd2bot.core.auth.authentificationManager import AuthentificationManager
from pyd2bot.core.network.message.msg import Msg
from time import sleep 
import json 

myAuthMgr = AuthentificationManager()
myAuthMgr.initAESKey()
sock = socket.socket()
auth_host = "54.76.16.121"
port = 5555
counter = 0

with open("account.json") as fp:
    auth_json = json.load(fp)
    login = auth_json["username"]
    password = auth_json["password"]
    
def handle(msg: Msg):
    print("received: ", msg.msgType["name"])
    mjson = msg.json()
    if msg.msgType["name"] == "HelloConnectMessage":
        myAuthMgr.setSalt(mjson["salt"])
        imsg: Msg = myAuthMgr.getIdentificationMessage("kmajdoub", "rMrTXHA4*")
        imsg.count = counter + 1
        data = imsg.bytes()
        sock.sendall(data)
    if msg.msgType["name"] == "IdentificationFailedMessage":
        print(mjson)
        
mdsniffer = DofusSniffer(handle)
mdsniffer.start()
sock.connect((auth_host, port))
sleep(60)