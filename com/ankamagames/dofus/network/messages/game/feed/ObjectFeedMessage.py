from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemQuantity import ObjectItemQuantity


class ObjectFeedMessage(INetworkMessage):
    protocolId = 5845
    objectUID:int
    meal:ObjectItemQuantity
    
    
