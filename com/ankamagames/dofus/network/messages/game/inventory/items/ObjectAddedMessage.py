from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class ObjectAddedMessage(NetworkMessage):
    protocolId = 9659
    object:ObjectItem
    origin:int
    
