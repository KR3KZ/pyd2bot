import logging
import threading
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pyd2bot.logic.frames import IFrame
    from pyd2bot.logic.managers import EventsManager
    from pyd2bot.network.connection import Connection
from pyd2bot.network.message import Message, Buffer
logger = logging.getLogger("bot")



class MsgListner(threading.Thread):
    
    def __init__(self, evtMgr:'EventsManager', conn:'Connection', frames:list['IFrame']):
        super().__init__(name="MsgListner")
        self._kill = threading.Event()
        self._buf = Buffer()
        self.evtMgr = evtMgr
        self.conn = conn
        self.frames = frames


    def interrupt(self):
        self._kill.set()


    def run(self):
        logger.info("Connection thread started.")
        while not self._kill.is_set():
            try:
                rdata = self.conn._sock.recv(8192)
                self._buf += rdata
                msg = Message.fromRaw(self._buf, False)
                while msg:
                    jmsg = msg.json()
                    mtypr = jmsg["__type__"]
                    self.evtMgr.handle(jmsg)
                    for frame in self.frames:
                        if not frame._done:
                            if frame.process(mtypr, jmsg):
                                break
                    msg = Message.fromRaw(self._buf, False)
            except OSError as e:
                pass
            except Exception as e:
                logger.error("Error: ", exc_info=True)
                self._kill.set()
                break
        self.conn.close()
        logger.info("Connection thread ended")
        