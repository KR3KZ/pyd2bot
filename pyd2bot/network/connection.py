import logging
import signal
from sys import exc_info
import sys
from types import FunctionType
from typing import TYPE_CHECKING
from pyd2bot.network.protocol import DofusProtocol
if TYPE_CHECKING:
    from pyd2bot.bot import Bot
from time import sleep
from inspect import trace
import socket
import threading
import pyd2bot.logic.frames as frames
from pyd2bot.network.message import Msg
from pyd2bot.utils.binaryIO import Buffer
logger = logging.getLogger("bot")


class KillSig(threading.Event):
    
    def __init__(self) -> None:
        super().__init__()
        self._childes = list[threading.Event]()

    def register(self, child:threading.Event) -> None:
        self._childes.append(child)

    def unregister(self, child:threading.Event) -> None:
        self._childes.remove(child)

    def set(self) -> None:
        super().set()
        for child in self._childes:
            child.set()

class Connection(threading.Thread):
    PORT = 5555
    # "54.76.16.121"
    AUTH_SERVER = "34.249.202.222" 

    def __init__(self, bot:'Bot'):
        super().__init__(name=bot.name)
        self.bot = bot
        self._sock = socket.socket()
        self._kill = KillSig()
        self._buf = Buffer()
        self._counter = 0
        self.frames:list[frames.IFrame] = [cls_frame(self) for cls_frame in frames._cls_frames]
        self.gameServer = None
        self.serverInfos = None
        self._callBacks = dict[str, list[tuple[FunctionType, bool, list[dict]]]]()
        signal.signal(signal.SIGINT, self.interrupt)

    def connectToLoginServer(self):
        self._sock = socket.socket()
        self._sock.connect((self.AUTH_SERVER, self.PORT))
        logger.info(f"Logging to auth server {self.AUTH_SERVER} on port {self.PORT}")
    
    
    def closeConnection(self):
        self._sock.close()
    
    
    def interrupt(self, signal=None, frame=None):
        self._kill.set()
    
    def connectToGameServer(self):
        self._sock = socket.socket()
        self._sock.connect((self.gameServer, self.PORT))
        

    def run(self):
        logger.info("Connection thread started.")
        while not self._kill.is_set():
            try:
                rdata = self._sock.recv(8192)
                self._buf += rdata
                msg = Msg.fromRaw(self._buf, False)
                while msg:
                    jmsg = msg.json()
                    logger.debug(f"recveived: {jmsg['__type__']}")
                    self.checkCallBacks(jmsg)
                    self.handle(jmsg)
                    msg = Msg.fromRaw(self._buf, False)
            except OSError as e:
                pass
            except Exception as e:
                logger.error("Error: ", exc_info=True)
                self.interrupt()
                break
        self._sock.close()
        logger.info("Connection thread ended")

          
    def send(self, msgjson):
        logger.debug("Sending: {0}".format(msgjson))
        try:
            msg = Msg.from_json(msgjson)
            self._counter += 1
            msg.count = self._counter 
            self._sock.sendall(msg.bytes())
        except OSError as e:
            pass
        finally:
            logger.debug("Sent")   
    

    def handle(self, msg: dict):
        mtype = msg["__type__"]
        for frame in self.frames:
            if not frame._done:
                if frame.process(mtype, msg):
                    return


    def checkCallBacks(self, msg):
        mtype = msg["__type__"]
        if mtype in self._callBacks:
            logger.debug("callback for msg {0} called.".format(mtype))
            for func, oneShot, ret in self._callBacks[mtype]:
                try:
                    r = func(msg)
                    if ret is not None:
                        ret.append(r)
                except:
                    logger.error("Error in callback: ", exc_info=True)
                if oneShot:
                    self._callBacks[mtype].remove((func, oneShot, ret))


    def registerOnMsgCallback(self, msgName:str, func:FunctionType, oneShot:bool=True, ret:list[dict]=None):
        if not Msg.protocol.getMsgTypeByName(msgName):
            raise ValueError("Unknown msgName: {0}".format(msgName))
        if msgName not in self._callBacks:
            self._callBacks[msgName] = []
        self._callBacks[msgName].append((func, oneShot, ret))
    

    def waitMsg(self, msgName:str, filter:FunctionType=None, timeout:int=20):
        if not filter:
            filter = lambda _: True
        event = threading.Event()
        self._kill.register(event)
        callback = lambda msg: event.set() if filter(msg) else None
        ret = []
        self.registerOnMsgCallback(msgName, callback , ret=ret)
        res = event.wait(timeout) and not self._kill.is_set()
        self._kill.unregister(event)
        return ret if res else None
