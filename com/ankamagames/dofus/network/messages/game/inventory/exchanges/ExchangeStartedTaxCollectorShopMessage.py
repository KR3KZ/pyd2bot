from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class ExchangeStartedTaxCollectorShopMessage(INetworkMessage):
    protocolId = 2236
    objects:ObjectItem
    kamas:int
    
    