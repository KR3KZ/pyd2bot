from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import ExchangeObjectMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


@dataclass
class ExchangeObjectAddedMessage(ExchangeObjectMessage):
    object:ObjectItem
    
    
    def __post_init__(self):
        super().__init__()
    