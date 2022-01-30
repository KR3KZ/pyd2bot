import logging
import socket
from pyd2bot.network.message import Message
logger = logging.getLogger("bot")

class Connection:
    PORT = 5555
    # "54.76.16.121"
    AUTH_SERVER = "34.249.202.222" 

    def __init__(self):
        self._sock = socket.socket()
        self.gameServer = None
        self.serverInfos = None
        self._counter = 0

    def connectToLoginServer(self):
        self._sock = socket.socket()
        self._sock.connect((self.AUTH_SERVER, self.PORT))
        logger.info(f"Logging to auth server {self.AUTH_SERVER} on port {self.PORT}")
    
    def close(self):
        self._sock.close()
    
    def connectToGameServer(self):
        self._sock = socket.socket()
        self._sock.connect((self.gameServer, self.PORT))
        logger.info(f"Logging to game server {self.gameServer} on port {self.PORT}")

    def send(self, msgjson):
        logger.debug("Sending: {0}".format(msgjson))
        try:
            msg = Message.from_json(msgjson)
            self._counter += 1
            msg.count = self._counter 
            self._sock.sendall(msg.serialize())
        except OSError as e:
            pass 
        logger.debug("Sent message {0}".format(msgjson["__type__"]))


            
