from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMoveMessage import ExchangeObjectMoveMessage


@dataclass
class ExchangeObjectMovePricedMessage(ExchangeObjectMoveMessage):
    price:int
    
    
    def __post_init__(self):
        super().__init__()
    