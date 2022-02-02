from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeRequestedMessage import ExchangeRequestedMessage


@dataclass
class ExchangeRequestedTradeMessage(ExchangeRequestedMessage):
    source:int
    target:int
    
    
    def __post_init__(self):
        super().__init__()
    