from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemQuantityPriceDateEffects import ObjectItemQuantityPriceDateEffects
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemQuantityPriceDateEffects import ObjectItemQuantityPriceDateEffects


class ExchangeOfflineSoldItemsMessage(INetworkMessage):
    protocolId = 5671
    bidHouseItems:ObjectItemQuantityPriceDateEffects
    merchantItems:ObjectItemQuantityPriceDateEffects
    
    
