from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeCraftResultMessage import ExchangeCraftResultMessage


@dataclass
class ExchangeCraftResultWithObjectIdMessage(ExchangeCraftResultMessage):
    objectGenericId:int
    
    
    def __post_init__(self):
        super().__init__()
    