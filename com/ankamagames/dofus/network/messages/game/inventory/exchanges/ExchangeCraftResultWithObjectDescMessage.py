from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeCraftResultMessage import ExchangeCraftResultMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItemNotInContainer import ObjectItemNotInContainer
    


class ExchangeCraftResultWithObjectDescMessage(ExchangeCraftResultMessage):
    objectInfo:'ObjectItemNotInContainer'
    

    def init(self, objectInfo:'ObjectItemNotInContainer', craftResult:int):
        self.objectInfo = objectInfo
        
        super().__init__(craftResult)
    
    