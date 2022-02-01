from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class ObjectModifiedMessage(NetworkMessage):
    object:ObjectItem
    
    
