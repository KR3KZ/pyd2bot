from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pyd2bot.network.connection import Connection


class IFrame:

    def __init__(self, conn:'Connection'):
        self.bot = conn.bot
        self.conn = conn
        self._done = False


    def handleConnectionOpened(self):
        pass
    

    def handleConnectionClosed(self):
        pass


    def process(self, msg:dict):
        pass