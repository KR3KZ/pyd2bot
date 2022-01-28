import logging
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pyd2bot.bot import IBot
import random
from pyd2bot.logic.frames import IFrame

class ServerRandRequestsFrame(IFrame):

    def __init__(self, bot:'IBot'):
        super().__init__(bot)
        self.seq = 1

    def process(self, mtype, msg) -> bool:

        if mtype == "SequenceNumberRequestMessage":
            self.conn.send({'__type__': 'SequenceNumberMessage', 'number': self.seq})
            self.seq += 1
            return True

        elif mtype == "BasicLatencyStatsRequestMessage":
            r = random.randint(25, 90)
            self.conn.send({
                '__type__': 'BasicLatencyStatsMessage',
                'latency': r,
                'max': r + 20,
                'sampleCount': random.randint(5, 10)
            })
            return True
        return False



