from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItemQuantityPriceDateEffects import ObjectItemQuantityPriceDateEffects
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItemQuantityPriceDateEffects import ObjectItemQuantityPriceDateEffects
    


class ExchangeOfflineSoldItemsMessage(NetworkMessage):
    bidHouseItems:list['ObjectItemQuantityPriceDateEffects']
    merchantItems:list['ObjectItemQuantityPriceDateEffects']
    

    def init(self, bidHouseItems:list['ObjectItemQuantityPriceDateEffects'], merchantItems:list['ObjectItemQuantityPriceDateEffects']):
        self.bidHouseItems = bidHouseItems
        self.merchantItems = merchantItems
        
        super().__init__()
    
    