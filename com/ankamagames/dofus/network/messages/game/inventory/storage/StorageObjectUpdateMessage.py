from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class StorageObjectUpdateMessage(INetworkMessage):
    protocolId = 728
    object:ObjectItem
    
    
