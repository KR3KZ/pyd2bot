from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSell import ObjectItemToSell
    


class ExchangeShopStockMovementUpdatedMessage(NetworkMessage):
    objectInfo:'ObjectItemToSell'
    

    def init(self, objectInfo:'ObjectItemToSell'):
        self.objectInfo = objectInfo
        
        super().__init__()
    
    