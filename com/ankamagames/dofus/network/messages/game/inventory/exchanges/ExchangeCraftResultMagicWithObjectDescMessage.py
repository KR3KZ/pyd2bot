from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeCraftResultWithObjectDescMessage import ExchangeCraftResultWithObjectDescMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItemNotInContainer import ObjectItemNotInContainer
    


class ExchangeCraftResultMagicWithObjectDescMessage(ExchangeCraftResultWithObjectDescMessage):
    magicPoolStatus:int
    

    def init(self, magicPoolStatus:int, objectInfo:'ObjectItemNotInContainer', craftResult:int):
        self.magicPoolStatus = magicPoolStatus
        
        super().__init__(objectInfo, craftResult)
    
    