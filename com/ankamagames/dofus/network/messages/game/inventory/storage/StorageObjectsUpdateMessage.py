from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class StorageObjectsUpdateMessage(INetworkMessage):
    protocolId = 7209
    objectList:ObjectItem
    
    
