import socket
import threading
from pyd2bot.network.customDataWrapper import Buffer
from pyd2bot.network.message import Msg
from pyd2bot.logic.auth.authentificationManager import AuthentificationManager
from pyd2bot.gameData.enums.IdentificationFailureReasons import IdentificationFailureReason
import pyd2bot.utils.crypto as crypto_utils

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
        self._serverId = None
        self.buf = Buffer()
        self.authManager = AuthentificationManager()
        self.killSig = threading.Event()
        self.inServerSelection = threading.Event()
        self.connected = threading.Event()
        self.counter = 0
        self.playerInfos = None
    
    def start(self, conn):
        self._login = conn["login"]
        self._password = conn["password"]
        self._serverId = conn["serverID"]
        super().start()
        
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
    
    def sendMsg(self, msg: Msg):
        msg.count = self.counter + 1
        self.sock.sendall(msg.bytes())
        self.counter = 3
        
    def handle(self, msg: Msg):
        jmsg = msg.json()
        mtype = msg.msgName["name"]
        print(jmsg)
        
        if mtype == "HelloConnectMessage":
            self.authManager.setSalt(jmsg["salt"])
            self.authManager.setPublicKey(jmsg["key"])
            imsg: Msg = self.authManager.getIdentificationMessage(self._login, self._password)
            self.sendMsg(imsg)
            kmsg = Msg.from_json({'__type__': 'ClientKeyMessage', 'key': 'LQ9r8NAvccW6G5cmD8#01'})
            self.sendMsg(kmsg)
            
        elif mtype == "IdentificationFailedMessage":
            print(jmsg["reason"], IdentificationFailureReason.WRONG_CREDENTIALS)
            if IdentificationFailureReason(jmsg["reason"]) == IdentificationFailureReason.WRONG_CREDENTIALS:
                self.killSig.set()

        elif mtype == "IdentificationSuccessMessage":
            self.playerInfos = jmsg
        
        elif mtype == "ServersListMessage":
            ssmsg = Msg.from_json({'__type__': 'ServerSelectionMessage', 'serverId': self._serverId})
            self.sendMsg(ssmsg)
        
        elif mtype == "SelectedServerDataMessage":
            self.serverInfos = jmsg
            self.sock.close()
            self.sock.connect((self.serverInfos["address"], self.port))
            bcypher_ticket = crypto_utils.intArrToBytesArr(self.serverInfos["ticket"])
            bticket = crypto_utils.decodeWithAES(self.authManager._AESKey, bcypher_ticket)
            ticket = crypto_utils.bytesToStr(bticket)
            ticketMsg = {
                '__type__': 'AuthenticationTicketMessage',
                'lang': 'fr',
                'ticket': ticket
            }
            self.sendMsg(ticketMsg)
        
        elif mtype == "RawDataMessage":
            content = bytearray()
            signature = Signature(SIGNATURE_KEY_V1, SIGNATURE_KEY_V2)
            _log.info("Bytecode len: " + rdMsg.content.length + ", hash: " + MD5.hashBytes(rdMsg.content))
            rdMsg.content.position = 0
            if(signature.verify(rdMsg.content,content)):
                l = Loader()
                LogInFile.getInstance().logLine("Kernel l.uncaughtErrorEvents.addEventListener onUncaughtError",FileLoggerEnum.EVENTLISTENERS)
                l.uncaughtErrorEvents.addEventListener(UncaughtErrorEvent.UNCAUGHT_ERROR,this.onUncaughtError,false,0,true)
                lc = LoaderContext(false,ApplicationDomain(ApplicationDomain.currentDomain))
                AirScanner.allowByteCodeExecution(lc,true)
                l.loadBytes(content,lc)
                        
            
        
        
