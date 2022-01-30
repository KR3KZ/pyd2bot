from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemQuantity import ObjectItemQuantity


class ObjectFeedMessage(NetworkMessage):
    protocolId = 5845
    objectUID:int
    meal:list[ObjectItemQuantity]
    
