from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSell import ObjectItemToSell
    


class ExchangeShopStockMultiMovementUpdatedMessage(NetworkMessage):
    objectInfoList:list['ObjectItemToSell']
    

    def init(self, objectInfoList:list['ObjectItemToSell']):
        self.objectInfoList = objectInfoList
        
        super().__init__()
    
    