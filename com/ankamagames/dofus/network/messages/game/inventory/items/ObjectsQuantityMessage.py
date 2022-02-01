from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemQuantity import ObjectItemQuantity


class ObjectsQuantityMessage(NetworkMessage):
    objectsUIDAndQty:list[ObjectItemQuantity]
    
    
