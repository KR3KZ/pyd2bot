from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class ExchangeStartedMountStockMessage(INetworkMessage):
    protocolId = 5729
    objectsInfos:ObjectItem
    
    
