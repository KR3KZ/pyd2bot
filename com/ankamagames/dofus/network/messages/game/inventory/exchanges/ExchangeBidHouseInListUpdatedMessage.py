from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseInListAddedMessage import ExchangeBidHouseInListAddedMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
    


class ExchangeBidHouseInListUpdatedMessage(ExchangeBidHouseInListAddedMessage):
    

    def init(self, itemUID:int, objectGID:int, objectType:int, effects:list['ObjectEffect'], prices:list[int]):
        
        super().__init__(itemUID, objectGID, objectType, effects, prices)
    
    