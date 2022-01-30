from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemQuantityPriceDateEffects import ObjectItemQuantityPriceDateEffects
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemQuantityPriceDateEffects import ObjectItemQuantityPriceDateEffects


class ExchangeOfflineSoldItemsMessage(NetworkMessage):
    protocolId = 5671
    bidHouseItems:ObjectItemQuantityPriceDateEffects
    merchantItems:ObjectItemQuantityPriceDateEffects
    
    
