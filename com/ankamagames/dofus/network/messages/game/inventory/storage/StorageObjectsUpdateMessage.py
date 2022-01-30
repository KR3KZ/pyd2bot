from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class StorageObjectsUpdateMessage(NetworkMessage):
    protocolId = 7209
    objectList:list[ObjectItem]
    
