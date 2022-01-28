from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pyd2bot.bot import IBot



class IFrame:

    def __init__(self, bot:'IBot'):
        self.bot = bot
        self.conn = bot.conn
        self._done = False

    def process(self, mtype:str, msg:dict) -> bool:
        pass