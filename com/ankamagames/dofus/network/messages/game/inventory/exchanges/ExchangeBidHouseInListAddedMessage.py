from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
    


class ExchangeBidHouseInListAddedMessage(NetworkMessage):
    itemUID:int
    objectGID:int
    objectType:int
    effects:list['ObjectEffect']
    prices:list[int]
    

    def init(self, itemUID:int, objectGID:int, objectType:int, effects:list['ObjectEffect'], prices:list[int]):
        self.itemUID = itemUID
        self.objectGID = objectGID
        self.objectType = objectType
        self.effects = effects
        self.prices = prices
        
        super().__init__()
    
    