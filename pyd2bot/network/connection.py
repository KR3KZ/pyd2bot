import logging
from sys import exc_info
from types import FunctionType
from typing import TYPE_CHECKING

from pyd2bot.network.protocol import DofusProtocol
if TYPE_CHECKING:
    from pyd2bot.bot import Bot
from time import sleep
from inspect import trace
import socket
import threading
import traceback
import pyd2bot.logic as logic
from pyd2bot.network.message import Msg
from pyd2bot.utils.binaryIO import Buffer
logger = logging.getLogger("bot")


class Connection(threading.Thread):
    PORT = 5555
    AUTH_SERVER = "54.76.16.121"

    def __init__(self, bot:'Bot'):
        super().__init__(name=bot.name)
        self.bot = bot
        self._sock = socket.socket()
        self._killSig = threading.Event()
        self._buf = Buffer()
        self._counter = 0
        self.frames:list[logic.IFrame] = [cls_frame(self) for cls_frame in logic._cls_frames]
        self.gameServer = None
        self.serverInfos = None
        self._callBacks = dict[str, list[FunctionType]]()
    
    def connectToLoginServer(self):
        self._sock = socket.socket()
        self._sock.connect((self.AUTH_SERVER, self.PORT))
    
    
    def closeConnection(self):
        self._sock.close()
    
    
    def interrupt(self):
        self._sock.close()
        self._killSig.set()

    
    def connectToGameServer(self):
        self._sock = socket.socket()
        self._sock.connect((self.gameServer, self.PORT))
        

    def run(self):
        logger.info("Connection thread started.")
        while not self._killSig.is_set():
            try:
                rdata = self._sock.recv(8192)
                self._buf += rdata
                msg = Msg.fromRaw(self._buf, False)
                while msg:
                    self.checkCallBacks(msg.json())
                    self.handle(msg.json())
                    msg = Msg.fromRaw(self._buf, False)
            except OSError:
                pass
            except:
                logger.error("Error: ", exc_info=True)
                self.interrupt()
                break
        logger.info("main thread ended")

          
    def send(self, msgjson):
        msg = Msg.from_json(msgjson)
        self._counter += 1
        msg.count = self._counter 
        self._sock.sendall(msg.bytes())
    
    
    def handle(self, msg: dict):
        for frame in self.frames:
                if frame.process(msg):
                    return


    def checkCallBacks(self, msg):
        mtype = msg["__type__"]
        if mtype in self._callBacks:
            logger.info("callback for msg {0} called.".format(mtype))
            for func, oneShot in self._callBacks[mtype]:
                try:
                    func(msg)
                except:
                    logger.error("Error in callback: ", exc_info=True)
                if oneShot:
                    self._callBacks[mtype].remove((func, oneShot))
            if not self._callBacks[mtype]:
                del self._callBacks[mtype]


    def registerOnMsgCallback(self, msgName:str, func:FunctionType, oneShot:bool=True):
        if not Msg.protocol.getMsgTypeByName(msgName):
            raise ValueError("Unknown msgName: {0}".format(msgName))
        if msgName not in self._callBacks:
            self._callBacks[msgName] = []
        self._callBacks[msgName].append((func, oneShot))
    

    def waitMsg(self, msgName:str, filter:FunctionType=None, timeout:int=20):
        if not filter:
            filter = lambda x: True
        event = threading.Event()
        callback = lambda msg: event.set() if filter(msg) else None
        self.registerOnMsgCallback(msgName, callback)
        return event.wait(timeout)

