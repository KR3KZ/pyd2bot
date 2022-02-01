from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemQuantity import ObjectItemQuantity


class ObjectsQuantityMessage(INetworkMessage):
    protocolId = 5570
    objectsUIDAndQty:ObjectItemQuantity
    
    
