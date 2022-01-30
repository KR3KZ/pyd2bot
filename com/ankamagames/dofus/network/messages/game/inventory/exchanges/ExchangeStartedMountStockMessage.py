from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class ExchangeStartedMountStockMessage(NetworkMessage):
    protocolId = 5729
    objectsInfos:ObjectItem
    
