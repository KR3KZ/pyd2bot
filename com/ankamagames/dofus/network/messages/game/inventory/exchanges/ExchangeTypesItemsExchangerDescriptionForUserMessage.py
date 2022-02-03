from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.BidExchangerObjectInfo import BidExchangerObjectInfo
    


class ExchangeTypesItemsExchangerDescriptionForUserMessage(NetworkMessage):
    objectType:int
    itemTypeDescriptions:list['BidExchangerObjectInfo']
    

    def init(self, objectType:int, itemTypeDescriptions:list['BidExchangerObjectInfo']):
        self.objectType = objectType
        self.itemTypeDescriptions = itemTypeDescriptions
        
        super().__init__()
    
    