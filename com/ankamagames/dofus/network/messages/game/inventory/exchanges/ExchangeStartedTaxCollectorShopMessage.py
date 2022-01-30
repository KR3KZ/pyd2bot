from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class ExchangeStartedTaxCollectorShopMessage(NetworkMessage):
    protocolId = 2236
    objects:ObjectItem
    kamas:int
    
