from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class ObjectsAddedMessage(NetworkMessage):
    protocolId = 1568
    object:ObjectItem
    
