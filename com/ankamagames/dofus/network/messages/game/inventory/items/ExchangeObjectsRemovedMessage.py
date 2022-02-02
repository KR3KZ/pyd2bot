from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import ExchangeObjectMessage


@dataclass
class ExchangeObjectsRemovedMessage(ExchangeObjectMessage):
    objectUID:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    