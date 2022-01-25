import functools
from re import S
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pyd2bot.network.connection import Connection



class IFrame:

    def __init__(self, conn:'Connection'):
        self.bot = conn.bot
        self.conn = conn
        self._done = False

    def process(self, mtype:str, msg:dict) -> bool:
        pass

    def handleConnectionOpened(self):
        pass

    def handleConnectionClosed(self):
        pass
