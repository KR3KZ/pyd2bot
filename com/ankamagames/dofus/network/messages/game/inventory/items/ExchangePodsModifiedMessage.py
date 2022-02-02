from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import ExchangeObjectMessage


@dataclass
class ExchangePodsModifiedMessage(ExchangeObjectMessage):
    currentWeight:int
    maxWeight:int
    
    
    def __post_init__(self):
        super().__init__()
    