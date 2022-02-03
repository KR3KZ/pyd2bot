from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSell import ObjectItemToSell
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
    


class ObjectItemToSellInBid(ObjectItemToSell):
    unsoldDelay:int
    

    def init(self, unsoldDelay:int, objectGID:int, effects:list['ObjectEffect'], objectUID:int, quantity:int, objectPrice:int):
        self.unsoldDelay = unsoldDelay
        
        super().__init__(objectGID, effects, objectUID, quantity, objectPrice)
    
    