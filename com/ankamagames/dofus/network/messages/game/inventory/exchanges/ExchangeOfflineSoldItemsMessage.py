from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemQuantityPriceDateEffects import ObjectItemQuantityPriceDateEffects
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemQuantityPriceDateEffects import ObjectItemQuantityPriceDateEffects


class ExchangeOfflineSoldItemsMessage(NetworkMessage):
    bidHouseItems:list[ObjectItemQuantityPriceDateEffects]
    merchantItems:list[ObjectItemQuantityPriceDateEffects]
    
    
