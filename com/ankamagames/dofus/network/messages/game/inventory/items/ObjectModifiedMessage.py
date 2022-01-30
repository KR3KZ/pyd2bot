from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class ObjectModifiedMessage(NetworkMessage):
    protocolId = 2793
    object:ObjectItem
    
    
