from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class StorageObjectUpdateMessage(NetworkMessage):
    protocolId = 728
    object:ObjectItem
    
    
