from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeRequestMessage import ExchangeRequestMessage


@dataclass
class ExchangePlayerRequestMessage(ExchangeRequestMessage):
    target:int
    
    
    def __post_init__(self):
        super().__init__()
    