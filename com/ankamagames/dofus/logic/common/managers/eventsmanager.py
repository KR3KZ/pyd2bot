
from ast import FunctionType
import logging
import threading
from pyd2bot.network.message import Message
logger = Logger(__name__)


class KillSig(threading.Event):
    
    def __init__(self) -> None:
        super().__init__()
        self._childes = list[threading.Event]()

    def register(self, child:threading.Event) -> None:
        if child not in self._childes:
            self._childes.append(child)

    def unregister(self, child:threading.Event) -> None:
        self._childes.remove(child)

    def set(self) -> None:
        super().set()
        for child in self._childes:
            child.set()


class EventsManager:

    def __init__(self):
        self._kill = KillSig()
        self._callBacks = dict[str, list[tuple[FunctionType, bool, list[dict]]]]()

    def interrupt(self):
        self._kill.set()

    def handle(self, msg):
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
        if not Message.parser.getMsgSpecByName(msgName):
            raise ValueError("Unknown msgName: {0}".format(msgName))
        if msgName not in self._callBacks:
            self._callBacks[msgName] = []
        self._callBacks[msgName].append((func, oneShot, ret))
    
    def bind(self, event, msgName, condition):
        if not condition:
            condition = lambda _: True
        self._kill.register(event)
        callback = lambda msg: event.set() if condition(msg) else None
        ret = []
        self.registerOnMsgCallback(msgName, callback , ret=ret)
        return ret

    def waitMsg(self, msgName:str, condition:FunctionType=None, timeout:int=20):
        event = threading.Event()
        ret = self.bind(event, msgName, condition)
        res = event.wait(timeout) and not self._kill.is_set()
        self._kill.unregister(event)
        return ret if res else None
    
    def waitMsgs(self, events:tuple[str, FunctionType], timeout:int=20):
        event = threading.Event()
        ret = {}
        for msgName, condition in events:        
            ret[msgName] = self.bind(event, msgName, condition)
        res = event.wait(timeout) and not self._kill.is_set()
        self._kill.unregister(event)
        return ret if res else None