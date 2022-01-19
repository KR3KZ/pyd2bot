import socket
import threading
from pyd2bot.network.customDataWrapper import Buffer
from pyd2bot.network.message import Msg
from pyd2bot.logic.auth.authentificationManager import AuthentificationManager
from pyd2bot.gameData.enums.IdentificationFailureReasons import IdentificationFailureReason

sock = socket.socket()
counter = 0

class DofusClient(threading.Thread):
    
    def __init__(self):
        super().__init__()
        self.sock = socket.socket()
        self.port = 5555
        self.server_ip = None
        self.auth_server_ip = "54.76.16.121"
        self._login = None
        self._password = None
        self.buf = Buffer()
        self.authManager = AuthentificationManager()
        self.killSig = threading.Event()
        self.counter = 0
        
    def run(self):
        self.sock.connect((self.auth_server_ip, self.port))
        while not self.killSig.is_set():
            rdata = self.sock.recv(8192)
            self.buf += rdata
            msg = Msg.fromRaw(self.buf, False)
            while msg:
                self.handle(msg)
                msg = Msg.fromRaw(self.buf, False)

    def interrupt(self):
        self.killSig.set()
        
    def handle(self, msg: Msg):
        jmsg = msg.json()
        mtype = msg.msgType["name"]
        print(jmsg)
        if mtype == "HelloConnectMessage":
            self.authManager.setSalt(jmsg["salt"])
            self.authManager.setPublicKey(jmsg["key"])
            imsg: Msg = self.authManager.getIdentificationMessage(self._login, self._password)
            imsg.count = self.counter + 1
            self.sock.sendall(imsg.bytes())
            self.counter = 3
            kmsg = Msg.from_json({'__type__': 'ClientKeyMessage', 'key': 'LQ9r8NAvccW6G5cmD8#01'})
            kmsg.count = self.counter + 1
            self.sock.sendall(kmsg.bytes())
            self.counter += 1

            self.counter += 1
        if mtype == "IdentificationFailedMessage":
            print(jmsg["reason"], IdentificationFailureReason.WRONG_CREDENTIALS)
            if IdentificationFailureReason(jmsg["reason"]) == IdentificationFailureReason.WRONG_CREDENTIALS:
                self.killSig.set()
