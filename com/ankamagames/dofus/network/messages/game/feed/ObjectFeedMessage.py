from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemQuantity import ObjectItemQuantity


class ObjectFeedMessage(NetworkMessage):
    objectUID:int
    meal:list[ObjectItemQuantity]
    
    
