from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeCraftResultMessage import ExchangeCraftResultMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemNotInContainer import ObjectItemNotInContainer


@dataclass
class ExchangeCraftResultWithObjectDescMessage(ExchangeCraftResultMessage):
    objectInfo:ObjectItemNotInContainer
    
    
    def __post_init__(self):
        super().__init__()
    