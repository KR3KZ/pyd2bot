from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
    


class BidExchangerObjectInfo(NetworkMessage):
    objectUID:int
    objectGID:int
    objectType:int
    effects:list['ObjectEffect']
    prices:list[int]
    

    def init(self, objectUID:int, objectGID:int, objectType:int, effects:list['ObjectEffect'], prices:list[int]):
        self.objectUID = objectUID
        self.objectGID = objectGID
        self.objectType = objectType
        self.effects = effects
        self.prices = prices
        
        super().__init__()
    
    