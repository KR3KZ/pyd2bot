from time import sleep
from inspect import trace
import socket
import threading
import traceback
from pyd2bot.network.message import Msg, ByteArray, Buffer
from pyd2bot.logic.connection.managers import AuthentificationManager
from pyd2bot.gameData.enums.IdentificationFailureReasons import IdentificationFailureReason
import math
import random
from pyd2bot.utils.crypto import RSA, RSACipher, PKCS1


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
        jmsg = msg.json()
        mtype = msg.name
        
        if mtype == "HelloConnectMessage":
            self.authManager.setSalt(jmsg["salt"])
            self.authManager.setPublicKey(jmsg["key"])
            imsg: Msg = self.authManager.getIdentificationMessage(self._login, self._password)
            self.send(imsg)
            kmsg = {'__type__': 'ClientKeyMessage', 'key': 'LQ9r8NAvccW6G5cmD8#01'}
            self.send(kmsg)
            
        elif mtype == "IdentificationFailedMessage":
            print(jmsg["reason"], IdentificationFailureReason.WRONG_CREDENTIALS)
            if IdentificationFailureReason(jmsg["reason"]) == IdentificationFailureReason.WRONG_CREDENTIALS:
                self.killSig.set()

        elif mtype == "IdentificationSuccessMessage":
            self.playerInfos = jmsg
        
        elif mtype == "ServersListMessage":
            ssmsg = {'__type__': 'ServerSelectionMessage', 'serverId': self._serverId}
            self.send(ssmsg)
        
        elif mtype == "SelectedServerDataMessage":
            self.serverInfos = jmsg
            ba_ticket = self.authManager.decodeWithAES(self.serverInfos["ticket"])
            self.serverInfos["ticket"] = ba_ticket.decode()
            self.sock.close()
            self.counter = 0
            self.sock = socket.socket()
            self.sock.connect((self.serverInfos["address"], self.port))
        
        elif mtype == "HelloGameMessage":
            ticketMsg = {
                '__type__': 'AuthenticationTicketMessage',
                'lang': 'fr',
                'ticket': self.serverInfos["ticket"]
            }
            self.send(ticketMsg)
        
        elif mtype == "RawDataMessage":
            # Bypass humain check here
            gameServerTicket = self.serverInfos["ticket"]

            key = b"AKMBJ2YBJUHRsk8yptfOlcVLksJSCCSiWUryWD/vv6euIERWlfrWN0+Csf8UVG4CY"\
                b"qoz3hDBuaA3oe48W1xFADd5Bm+ks0dW3hemrTSI7HBLSLBWAcKrZ21wPfgWD2QUxVV1infGd"\
                b"pw+Lt0808UwqdDGUpwV2JGqzIbMZjGCXWdj8Ae2ribiXWU2P255Uv5nhC7O4ZKoTNXDAmjtc"\
                b"3qYzSXUZTkrhlf3yL8J/XyUvHuvuKetABtoJun2QaaKkuO6258oDtDxnKQKgKhtVrc0Jpa"\
                b"Qusr7GlWRcg6bK2M8dWjj+TAuwZLMvn7ltKYJjgvYymasrRu+56wbreTHa98ctVE="
                
            publicModulo = int.from_bytes(key, "big")
            rsaKeyNetwork = RSA.RsaKey(n=publicModulo, e=65537) 

            keyLen = 128
            hashKey = bytearray()
            i = 0
            while i < keyLen // 8:
                rb = math.floor(random.random() * 256) - 128
                hashKey += rb.to_bytes(1, "big", signed=True)
                i+=1
                
            xorKey2Len = math.floor(random.random() * 128) + 128
            xorKey2 = bytearray()
            i = 0
            while(i < xorKey2Len // 8):
                rb =  math.floor(random.random() * 256 - 128)
                xorKey2 += rb.to_bytes(1, "big", signed=True)
                i+=1 
            i = 0

            dataToEncrypt = ByteArray()
            dataToEncrypt.writeUTF(gameServerTicket)
            dataToEncrypt.writeShort(len(hashKey))
            dataToEncrypt += hashKey
            dataToEncrypt.writeShort(len(xorKey2))
            dataToEncrypt += xorKey2
            dataToEncrypt.position = 0

            dataIndex = 0
            while dataIndex < len(dataToEncrypt):
                dataToEncrypt[dataIndex] = 0 ^ 0
                dataIndex += 1

            rsacipher = RSACipher(rsaKeyNetwork, PKCS1())
            enc_data = rsacipher.encrypt(dataToEncrypt)
            ret = enc_data.to_int8Arr()
            self.send({
                '__type__': 'CheckIntegrityMessage',
                'data': ret
            })
            
        elif mtype == "TrustStatusMessage":
            self.connected.set()
            self.send({'__type__': 'CharactersListRequestMessage'})
            sleep(0.5)
            self.send({'__type__': 'CharacterSelectionMessage', 'id': 290210840786})
                        
        
        
