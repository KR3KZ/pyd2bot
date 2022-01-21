from time import sleep
from inspect import trace
import socket
import threading
import traceback
from pyd2bot.logic.common.managers.playerManager import PlayerManager
from pyd2bot.logic.connection.frames.authentificationFrame import AuthentificationFrame
from pyd2bot.logic.connection.frames.serverLoginFrame import ServerLoginFrame
from pyd2bot.logic.connection.managers import AuthentificationManager
from pyd2bot.gameData.enums.IdentificationFailureReasons import IdentificationFailureReason
from pyd2bot.network.message import Msg, ByteArray, Buffer

sock = socket.socket()
counter = 0

frameClasses = [AuthentificationFrame, ServerLoginFrame]

class DofusClient(threading.Thread):
    
    def __init__(self):
        super().__init__()
        self.sock = socket.socket()
        self.port = 5555
        self.game_server_host = None
        self.serverInfos = None
        self.auth_server_ip = "54.76.16.121"
        self._login = None
        self._password = None
        self.serverID = None
        self.buf = Buffer()
        self.authManager = AuthentificationManager()
        self.killSig = threading.Event()
        self.inServerSelection = threading.Event()
        self.connected = threading.Event()
        self.counter = 0
        self.login_attempts = 0
        self.frames = []
        for fc in frameClasses:
            self.frames.append(fc(self))
        

    def start(self, conn):
        self._login = conn["login"]
        self._password = conn["password"]
        PlayerManager.characterName = conn["characterName"]
        PlayerManager.serverID = int(conn["serverID"])
        super().start()
        
    def connectToLoginServer(self):
        self.sock = socket.socket()
        self.sock.connect((self.auth_server_ip, self.port))
    
    def connectToGameServer(self):
        self.sock = socket.socket()
        self.sock.connect((self.game_server_host, self.port))
        
    def stopConnection(self):
        self.sock.close() 
        
    def closeConnection(self):
        self.sock.close()
        self.killSig.set()
        
    def run(self):
        self.connectToLoginServer()
        while not self.killSig.is_set():
            try:
                rdata = self.sock.recv(8192)
                self.buf += rdata
                msg = Msg.fromRaw(self.buf, False)
                while msg:
                    self.handle(msg)
                    msg = Msg.fromRaw(self.buf, False)
            except Exception as e:
                traceback.print_exc()
                self.killSig.set()
                
    def interrupt(self):
        self.killSig.set()
    
    def send(self, msgjson):
        msg = Msg.from_json(msgjson)
        self.counter += 1
        msg.count = self.counter 
        self.sock.sendall(msg.bytes())
        
    def handle(self, msg: Msg): 
        for frame in self.frames:
            if frame.process(msg.json()):
                return
    